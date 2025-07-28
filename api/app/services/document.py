from typing import List, Optional, Dict, Any
from uuid import UUID
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from fastapi import UploadFile, HTTPException
import logging

from app.models.document import Document, DocumentStatus
from app.models.project import Project
from app.schemas.document import DocumentCreate, DocumentUpdate
from app.services.storage import storage_service
from app.services.message_queue import mq_service
from app.metrics import (
    documents_uploaded_total,
    documents_processed_total,
    storage_bytes_total,
    documents_in_queue
)

# Configure logger
logger = logging.getLogger(__name__)

class DocumentService:
    """Service for managing documents."""
    
    async def upload_document(
        self,
        db: AsyncSession,
        file: UploadFile,
        project_id: UUID,
        user_id: UUID
    ) -> Document:
        """
        Upload a Visio document and initiate parsing.
        
        Args:
            db: Database session
            file: Uploaded file
            project_id: Project UUID
            user_id: User UUID
            
        Returns:
            Created document record
        """
        logger.info(f"Starting document upload for project {project_id}, user {user_id}, file: {file.filename}")
        
        # Verify project exists and user owns it
        project_stmt = select(Project).where(
            Project.id == project_id,
            Project.owner_id == user_id
        )
        project_result = await db.execute(project_stmt)
        project = project_result.scalar_one_or_none()
        
        if not project:
            logger.error(f"Project {project_id} not found or user {user_id} doesn't have access")
            raise HTTPException(status_code=404, detail="Project not found")
        
        # Validate file type
        allowed_extensions = {".vsd", ".vsdx", ".vsdm"}
        file_extension = "".join(file.filename.split(".")[-1:])
        if f".{file_extension.lower()}" not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file type. Allowed types: {', '.join(allowed_extensions)}"
            )
        
        # Read file content
        file_content = await file.read()
        file_size = len(file_content)
        
        # Create document record
        document = Document(
            project_id=project_id,
            filename=file.filename.split("/")[-1],  # Get just the filename
            original_filename=file.filename,
            file_size=file_size,
            content_type=file.content_type or "application/vnd.visio",
            uploaded_by=user_id,
            status=DocumentStatus.UPLOADED
        )
        
        db.add(document)
        await db.commit()
        await db.refresh(document)
        
        try:
            # Upload file to storage
            storage_path = await storage_service.upload_visio_file(
                file_data=file_content,
                filename=document.filename,
                document_id=document.id,
                content_type=document.content_type
            )
            
            # Update document with storage path
            document.file_path = storage_path
            document.status = DocumentStatus.PARSING
            await db.commit()
            
            # Publish parse request to message queue
            await mq_service.publish_parse_request(
                document_id=document.id,
                file_path=storage_path,
                project_id=project_id
            )
            
        except Exception as e:
            # If upload fails, mark document as failed
            document.status = DocumentStatus.FAILED
            document.error_message = str(e)
            await db.commit()
            raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
        
        logger.info(f"Document upload completed successfully: {document.id}")
        return document
    
    async def get_document(
        self,
        db: AsyncSession,
        document_id: UUID,
        user_id: UUID
    ) -> Optional[Document]:
        """Get a document by ID, ensuring user has access."""
        stmt = select(Document).join(Project).where(
            Document.id == document_id,
            Project.owner_id == user_id
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def list_project_documents(
        self,
        db: AsyncSession,
        project_id: UUID,
        user_id: UUID
    ) -> List[Document]:
        """List all documents in a project."""
        stmt = select(Document).join(Project).where(
            Document.project_id == project_id,
            Project.owner_id == user_id
        ).order_by(Document.uploaded_at.desc())
        
        result = await db.execute(stmt)
        return result.scalars().all()
    
    async def list_user_documents(
        self,
        db: AsyncSession,
        user_id: UUID,
        skip: int = 0,
        limit: int = 100
    ) -> List[Document]:
        """List all documents for a user across all projects."""
        stmt = select(Document).join(Project).where(
            Project.owner_id == user_id
        ).order_by(Document.uploaded_at.desc()).offset(skip).limit(limit)
        
        result = await db.execute(stmt)
        return result.scalars().all()
    
    async def update_document_status(
        self,
        db: AsyncSession,
        document_id: UUID,
        status: DocumentStatus,
        error_message: Optional[str] = None,
        parsed_data: Optional[Dict[str, Any]] = None
    ):
        """Update document status (typically called by background workers)."""
        stmt = update(Document).where(
            Document.id == document_id
        ).values(
            status=status,
            error_message=error_message
        )
        
        if status == DocumentStatus.PARSED and parsed_data:
            stmt = stmt.values(
                parsed_at=datetime.utcnow(),
                shape_count=parsed_data.get("shape_count"),
                connection_count=parsed_data.get("connection_count"),
                page_count=parsed_data.get("page_count"),
                parsed_data_path=parsed_data.get("parsed_path")
            )
        elif status == DocumentStatus.COMPLETED:
            stmt = stmt.values(completed_at=datetime.utcnow())
            
        await db.execute(stmt)
        await db.commit()
    
    async def generate_documentation(
        self,
        db: AsyncSession,
        document_id: UUID,
        user_id: UUID,
        formats: List[str]
    ) -> Document:
        """
        Initiate documentation generation for a parsed document.
        
        Args:
            db: Database session
            document_id: Document UUID
            user_id: User UUID
            formats: List of output formats
            
        Returns:
            Updated document record
        """
        from app.models.user import User
        from app.models.organization import Organization
        from app.models.document_template import DocumentTemplate
        
        # Get document and verify access
        document = await self.get_document(db, document_id, user_id)
        
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
            
        if document.status != DocumentStatus.PARSED:
            raise HTTPException(
                status_code=400,
                detail=f"Document must be parsed before generating. Current status: {document.status}"
            )
        
        # Update status
        document.status = DocumentStatus.GENERATING
        await db.commit()
        
        # Get project details
        project_result = await db.execute(
            select(Project).where(Project.id == document.project_id)
        )
        project = project_result.scalar_one_or_none()
        
        project_metadata = {}
        template_data = {}
        organization_data = {}
        
        if project:
            # Build project metadata with customer info
            project_metadata = {
                "project_name": project.name,
                "project_description": project.description,
                "customer_name": project.customer_name or "",
                "customer_organization": project.customer_organization or "",
                "customer_contact_name": project.customer_contact_name or "",
                "customer_contact_email": project.customer_contact_email or "",
                "customer_contact_phone": project.customer_contact_phone or "",
                "project_code": project.project_code or "",
                "project_manager": project.project_manager or "",
                "contract_number": project.contract_number or "",
                "po_number": project.po_number or "",
                "start_date": project.start_date.isoformat() if project.start_date else "",
                "end_date": project.end_date.isoformat() if project.end_date else "",
                "budget": project.budget or "",
                "priority": project.priority or "medium"
            }
            
            # Get user's organization
            user_result = await db.execute(
                select(User).where(User.id == user_id)
            )
            user = user_result.scalar_one_or_none()
            
            if user and user.organization_id:
                # Get organization data
                org_result = await db.execute(
                    select(Organization).where(Organization.id == user.organization_id)
                )
                organization = org_result.scalar_one_or_none()
                
                if organization:
                    organization_data = {
                        "name": organization.name,
                        "display_name": organization.display_name or organization.name,
                        "logo_url": organization.logo_url,
                        "primary_color": organization.primary_color,
                        "secondary_color": organization.secondary_color,
                        "accent_color": organization.accent_color,
                        "default_font_family": organization.default_font_family,
                        "default_font_size": organization.default_font_size,
                        "address_line1": organization.address_line1,
                        "city": organization.city,
                        "state": organization.state,
                        "postal_code": organization.postal_code,
                        "country": organization.country
                    }
                    
                    # Get default template for organization
                    template_result = await db.execute(
                        select(DocumentTemplate).where(
                            DocumentTemplate.organization_id == organization.id,
                            DocumentTemplate.is_default == True,
                            DocumentTemplate.is_active == True
                        )
                    )
                    template = template_result.scalar_one_or_none()
                    
                    if not template:
                        # Fall back to system template
                        template_result = await db.execute(
                            select(DocumentTemplate).where(
                                DocumentTemplate.is_system_template == True,
                                DocumentTemplate.is_default == True,
                                DocumentTemplate.is_active == True
                            )
                        )
                        template = template_result.scalar_one_or_none()
                    
                    if template:
                        template_data = {
                            "html_template": template.html_template,
                            "css_styles": template.css_styles,
                            "header_template": template.header_template,
                            "footer_template": template.footer_template,
                            "cover_page_template": template.cover_page_template
                        }
        
        # Get AI analysis if enabled
        # TODO: Call AI service to get analysis
        ai_analysis = {}
        
        # Get supplemental data if any
        # TODO: Retrieve from document supplemental data
        supplemental_data = {}
        
        # Publish generation request with all data
        await mq_service.publish_generate_request(
            document_id=document.id,
            parsed_data_path=document.parsed_data_path,
            formats=formats,
            project_id=document.project_id,
            project_metadata=project_metadata,
            template_data=template_data,
            organization_data=organization_data,
            ai_analysis=ai_analysis,
            supplemental_data=supplemental_data
        )
        
        return document
    
    async def get_document_download_url(
        self,
        db: AsyncSession,
        document_id: UUID,
        user_id: UUID,
        format_type: str
    ) -> Optional[str]:
        """Get download URL for a generated document."""
        document = await self.get_document(db, document_id, user_id)
        
        if not document or not document.generated_files:
            return None
            
        file_path = document.generated_files.get(format_type)
        if not file_path:
            return None
            
        return storage_service.get_download_url(file_path)
    
    async def delete_document(
        self,
        db: AsyncSession,
        document_id: UUID,
        user_id: UUID
    ) -> bool:
        """Delete a document and its associated files."""
        document = await self.get_document(db, document_id, user_id)
        
        if not document:
            return False
            
        # Delete files from storage
        try:
            if document.file_path:
                # Extract bucket and object name from path
                parts = document.file_path.split("/", 1)
                if len(parts) == 2:
                    await storage_service.delete_file("uploads", parts[1])
                    
            # Delete generated files
            if document.generated_files:
                for file_path in document.generated_files.values():
                    parts = file_path.split("/", 1)
                    if len(parts) == 2:
                        await storage_service.delete_file("generated", parts[1])
        except Exception as e:
            # Log error but continue with database deletion
            print(f"Error deleting files: {e}")
        
        # Delete from database
        await db.delete(document)
        await db.commit()
        
        return True

# Global document service instance
document_service = DocumentService()