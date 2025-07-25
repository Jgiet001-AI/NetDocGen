from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from uuid import UUID
import io
import logging

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.document import (
    Document, DocumentUploadResponse, DocumentGenerateRequest,
    DocumentGenerateResponse
)
from app.models.document import Document as DocumentModel
from app.schemas.common import Message
from app.services.document import document_service
from app.services.storage import storage_service

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_visio_file(
    project_id: UUID = Query(..., description="Project ID to upload document to"),
    file: UploadFile = File(..., description="Visio file to upload"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Upload a Visio file for parsing."""
    logger.info(f"Received upload request from user {current_user.id} for project {project_id}")
    logger.debug(f"File details - name: {file.filename}, content_type: {file.content_type}, size: {file.size}")
    
    try:
        document = await document_service.upload_document(
            db=db,
            file=file,
            project_id=project_id,
            user_id=current_user.id
        )
        
        logger.info(f"Upload successful. Document ID: {document.id}, Status: {document.status}")
        
        return DocumentUploadResponse(
            id=document.id,
            filename=document.filename,
            status=document.status,
            message="File uploaded successfully. Parsing will begin shortly."
        )
    except HTTPException as he:
        logger.error(f"HTTP error during upload: {he.detail}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during upload: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred during file upload: {str(e)}. Please check the logs for details."
        )

@router.get("/{document_id}", response_model=Document)
async def get_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get document details."""
    document = await document_service.get_document(db, document_id, current_user.id)
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return document

@router.post("/{document_id}/generate", response_model=DocumentGenerateResponse)
async def generate_documentation(
    document_id: UUID,
    request: DocumentGenerateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Generate documentation from a parsed Visio file."""
    try:
        document = await document_service.generate_documentation(
            db=db,
            document_id=document_id,
            user_id=current_user.id,
            formats=request.formats
        )
        
        return DocumentGenerateResponse(
            document_id=document.id,
            status="processing",
            message=f"Documentation generation started for formats: {', '.join(request.formats)}"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{document_id}/refresh-status")
async def refresh_document_status(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Manually refresh document status from parsed data."""
    from app.models.document import DocumentStatus
    from sqlalchemy import update
    from datetime import datetime
    
    # Check if parsed data exists
    try:
        parsed_path = f"{document_id}/parsed_data.json"
        parsed_data = await storage_service.download_file("parsed", parsed_path)
        
        # Update document status
        await db.execute(
            update(DocumentModel)
            .where(DocumentModel.id == document_id)
            .values(
                status=DocumentStatus.PARSED,
                parsed_at=datetime.utcnow(),
                parsed_data_path=parsed_path
            )
        )
        await db.commit()
        
        return {"status": "success", "message": "Document status updated to parsed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/{document_id}/download/{format_type}")
async def download_document(
    document_id: UUID,
    format_type: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Download a generated document."""
    # Get document to verify access and get file path
    document = await document_service.get_document(db, document_id, current_user.id)
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    if not document.generated_files or format_type not in document.generated_files:
        raise HTTPException(
            status_code=404,
            detail=f"Document not available in {format_type} format"
        )
    
    # Get file path from generated files
    file_path = document.generated_files[format_type]
    bucket_type, object_name = file_path.split("/", 1)
    
    try:
        # Download file from storage
        file_data = await storage_service.download_file("generated", object_name)
        
        # Determine content type
        content_types = {
            "html": "text/html",
            "pdf": "application/pdf",
            "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "markdown": "text/markdown"
        }
        content_type = content_types.get(format_type, "application/octet-stream")
        
        # Return file as streaming response
        return StreamingResponse(
            io.BytesIO(file_data),
            media_type=content_type,
            headers={
                "Content-Disposition": f"attachment; filename={document.filename}.{format_type}"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading file: {str(e)}")

@router.delete("/{document_id}", response_model=Message)
async def delete_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a document and its associated files."""
    success = await document_service.delete_document(db, document_id, current_user.id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return Message(message="Document deleted successfully")

@router.get("", response_model=List[Document])
async def list_documents(
    project_id: Optional[UUID] = Query(None, description="Filter by project ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all documents for the current user, optionally filtered by project."""
    if project_id:
        documents = await document_service.list_project_documents(
            db, project_id, current_user.id
        )
    else:
        # Get all documents for the user across all projects
        documents = await document_service.list_user_documents(
            db, current_user.id, skip=skip, limit=limit
        )
    return documents

@router.get("/project/{project_id}", response_model=List[Document])
async def list_project_documents(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all documents in a project."""
    documents = await document_service.list_project_documents(
        db, project_id, current_user.id
    )
    return documents

@router.get("/debug/connectivity")
async def check_connectivity(
    current_user: User = Depends(get_current_user)
):
    """Debug endpoint to check RabbitMQ and MinIO connectivity."""
    from app.services.message_queue import mq_service
    from app.services.storage import storage_service
    
    results = {
        "rabbitmq": {"status": "unknown", "error": None},
        "minio": {"status": "unknown", "error": None}
    }
    
    # Check RabbitMQ
    try:
        await mq_service.connect()
        results["rabbitmq"]["status"] = "connected"
        logger.info("RabbitMQ connectivity check: SUCCESS")
    except Exception as e:
        results["rabbitmq"]["status"] = "failed"
        results["rabbitmq"]["error"] = str(e)
        logger.error(f"RabbitMQ connectivity check: FAILED - {str(e)}")
    
    # Check MinIO
    try:
        await storage_service.initialize()
        results["minio"]["status"] = "connected"
        logger.info("MinIO connectivity check: SUCCESS")
    except Exception as e:
        results["minio"]["status"] = "failed"
        results["minio"]["error"] = str(e)
        logger.error(f"MinIO connectivity check: FAILED - {str(e)}")
    
    return results