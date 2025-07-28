import os
import sys
import asyncio
import logging
from typing import Dict, Any
from uuid import UUID

from app.config import settings

# Import the shared message queue client
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
from shared.messaging.queue import MessageQueue, RoutingKeys

logger = logging.getLogger(__name__)

class MessageQueueService:
    """Service for handling message queue operations."""
    
    def __init__(self):
        self.mq = MessageQueue(settings.RABBITMQ_URL)
        self._connected = False
    
    async def connect(self):
        """Connect to the message queue."""
        if not self._connected:
            logger.info(f"Connecting to RabbitMQ at {settings.RABBITMQ_URL}")
            try:
                await self.mq.connect()
                self._connected = True
                logger.info("Successfully connected to RabbitMQ")
            except Exception as e:
                logger.error(f"Failed to connect to RabbitMQ: {str(e)}", exc_info=True)
                raise
    
    async def disconnect(self):
        """Disconnect from the message queue."""
        if self._connected:
            await self.mq.disconnect()
            self._connected = False
    
    async def publish_parse_request(
        self,
        document_id: UUID,
        file_path: str,
        project_id: UUID
    ):
        """
        Publish a request to parse a Visio file.
        
        Args:
            document_id: Document UUID
            file_path: Path to file in MinIO
            project_id: Project UUID
        """
        logger.info(f"Publishing parse request for document {document_id}")
        logger.debug(f"File path: {file_path}, Project ID: {project_id}")
        
        try:
            await self.connect()
            
            message = {
                "document_id": str(document_id),
                "file_path": file_path,
                "project_id": str(project_id)
            }
            
            logger.debug(f"Publishing message: {message}")
            await self.mq.publish(
                routing_key=RoutingKeys.PARSE_VISIO,
                message=message
            )
            logger.info(f"Parse request published successfully for document {document_id}")
        except Exception as e:
            logger.error(f"Failed to publish parse request for document {document_id}: {str(e)}", exc_info=True)
            raise
    
    async def publish_generate_request(
        self,
        document_id: UUID,
        parsed_data_path: str,
        formats: list[str],
        project_id: UUID,
        project_metadata: Dict[str, Any] = None,
        template_data: Dict[str, Any] = None,
        organization_data: Dict[str, Any] = None,
        ai_analysis: Dict[str, Any] = None,
        supplemental_data: Dict[str, Any] = None
    ):
        """
        Publish a request to generate documentation.
        
        Args:
            document_id: Document UUID
            parsed_data_path: Path to parsed data in MinIO
            formats: List of output formats
            project_id: Project UUID
            project_metadata: Project metadata including customer info
            template_data: Template configuration from database
            organization_data: Organization branding data
            ai_analysis: AI-enhanced content
            supplemental_data: User-provided supplemental info
        """
        await self.connect()
        
        message = {
            "document_id": str(document_id),
            "parsed_data_path": parsed_data_path,
            "formats": formats,
            "project_id": str(project_id),
            "project_metadata": project_metadata or {},
            "template": template_data or {},
            "organization": organization_data or {},
            "ai_analysis": ai_analysis or {},
            "supplemental_data": supplemental_data or {}
        }
        
        await self.mq.publish(
            routing_key=RoutingKeys.GENERATE_DOC,
            message=message
        )
    
    async def handle_parse_complete(self, message: Dict[str, Any]):
        """Handle parse completion messages."""
        from app.database import AsyncSessionLocal
        from app.models.document import Document, DocumentStatus
        from sqlalchemy import update, select
        from uuid import UUID
        from datetime import datetime
        
        document_id = message.get("document_id")
        if not document_id:
            logger.error("No document_id in parse complete message")
            return
        
        logger.info(f"Received parse complete message for document {document_id}")
        
        async with AsyncSessionLocal() as db:
            try:
                if message.get("status") == "completed":
                    await db.execute(
                        update(Document)
                        .where(Document.id == UUID(document_id))
                        .values(
                            status=DocumentStatus.PARSED,
                            parsed_at=datetime.utcnow(),
                            parsed_data_path=message.get("parsed_data_path"),
                            shape_count=message.get("shape_count", 0),
                            connection_count=message.get("connection_count", 0),
                            page_count=message.get("page_count", 0)
                        )
                    )
                    await db.commit()
                    
                    # Automatically trigger document generation after successful parsing
                    logger.info(f"Triggering document generation for {document_id}")
                    
                    # Get the document details
                    result = await db.execute(
                        select(Document).where(Document.id == UUID(document_id))
                    )
                    document = result.scalar_one_or_none()
                    
                    if document:
                        # Get project details for professional documentation
                        from app.models.project import Project
                        from app.models.user import User
                        from app.models.organization import Organization
                        from app.models.document_template import DocumentTemplate
                        
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
                                select(User).where(User.id == project.owner_id)
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
                        
                        await self.publish_generate_request(
                            document_id=UUID(document_id),
                            parsed_data_path=message.get("parsed_data_path"),
                            formats=["html", "pdf", "markdown"],  # Default formats
                            project_id=document.project_id,
                            project_metadata=project_metadata,
                            template_data=template_data,
                            organization_data=organization_data,
                            ai_analysis=ai_analysis,
                            supplemental_data=supplemental_data
                        )
                        logger.info(f"Document generation request published for {document_id}")
                else:
                    await db.execute(
                        update(Document)
                        .where(Document.id == UUID(document_id))
                        .values(
                            status=DocumentStatus.FAILED,
                            error_message=message.get("error", "Parsing failed")
                        )
                    )
                    await db.commit()
                logger.info(f"Updated document {document_id} after parsing")
            except Exception as e:
                logger.error(f"Error updating document {document_id}: {e}")
                await db.rollback()
    
    async def handle_generate_complete(self, message: Dict[str, Any]):
        """Handle generation completion messages."""
        from app.database import AsyncSessionLocal
        from app.models.document import Document, DocumentStatus
        from sqlalchemy import update
        from uuid import UUID
        from datetime import datetime
        
        document_id = message.get("document_id")
        if not document_id:
            logger.error("No document_id in generate complete message")
            return
        
        logger.info(f"Received generate complete message for document {document_id}")
        
        async with AsyncSessionLocal() as db:
            try:
                if message.get("status") == "completed":
                    await db.execute(
                        update(Document)
                        .where(Document.id == UUID(document_id))
                        .values(
                            status=DocumentStatus.COMPLETED,
                            completed_at=datetime.utcnow(),
                            generated_files=message.get("generated_files", {})
                        )
                    )
                else:
                    await db.execute(
                        update(Document)
                        .where(Document.id == UUID(document_id))
                        .values(
                            status=DocumentStatus.FAILED,
                            error_message=message.get("error", "Generation failed")
                        )
                    )
                await db.commit()
                logger.info(f"Updated document {document_id} after generation")
            except Exception as e:
                logger.error(f"Error updating document {document_id}: {e}")
                await db.rollback()
    
    async def setup_completion_handlers(self):
        """
        Set up handlers for completion messages.
        This would typically be called during app startup.
        """
        try:
            logger.info("Setting up completion handlers...")
            
            # Register message handlers
            await self.mq.consume("api_parse_complete", RoutingKeys.PARSE_COMPLETE, self.handle_parse_complete)
            await self.mq.consume("api_generate_complete", RoutingKeys.GENERATE_COMPLETE, self.handle_generate_complete)
            
            logger.info("Completion handlers registered successfully")
                
        except Exception as e:
            logger.error(f"Error setting up completion handlers: {e}")
            raise

# Global message queue service instance
mq_service = MessageQueueService()