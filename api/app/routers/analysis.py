"""
Document Enhancement API endpoints using LLM
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Dict, Any, List

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.document import Document
from app.services.llm.document_assistant import DocumentAssistant
from app.services.storage import storage_service
import json

router = APIRouter()

@router.post("/documents/{document_id}/enhance")
async def enhance_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Enhance document with AI-generated content
    
    This endpoint uses AI to improve documentation quality by providing:
    - Professional executive summary
    - Technical glossary
    - Enhanced device descriptions
    - Clear connection explanations
    - Suggested documentation structure
    """
    # Get document
    document = await db.get(Document, document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    # Check if document is processed
    if document.status != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Document must be processed before enhancement"
        )
    
    # Get parsed data from storage
    try:
        parsed_data_path = f"parsed/{document_id}/parsed_data.json"
        parsed_json = await storage_service.download_file("parsed", f"{document_id}/parsed_data.json")
        parsed_data = json.loads(parsed_json.decode('utf-8'))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve parsed data: {str(e)}"
        )
    
    # Enhance documentation
    assistant = DocumentAssistant()
    try:
        enhancement_results = await assistant.enhance_documentation(parsed_data)
        
        # Store enhancement results
        enhancement_path = f"analysis/{document_id}/ai_enhancements.json"
        from io import BytesIO
        enhancement_json = json.dumps(enhancement_results, indent=2)
        await storage_service.upload_file(
            bucket_type="analysis",
            object_name=f"{document_id}/ai_enhancements.json",
            file_data=BytesIO(enhancement_json.encode()),
            content_type="application/json"
        )
        
        # Update document with enhancement status
        document.ai_analysis_completed = True
        await db.commit()
        
        return {
            "document_id": str(document_id),
            "enhancements": enhancement_results,
            "enhancement_path": enhancement_path
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Enhancement failed: {str(e)}"
        )

@router.get("/documents/{document_id}/enhancements")
async def get_document_enhancements(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Retrieve existing AI enhancements for a document
    """
    # Get document
    document = await db.get(Document, document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    # Check if enhancements exist
    try:
        enhancement_json = await storage_service.download_file(
            "analysis", 
            f"{document_id}/ai_enhancements.json"
        )
        enhancement_data = json.loads(enhancement_json.decode('utf-8'))
        
        return {
            "document_id": str(document_id),
            "enhancements": enhancement_data
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enhancements not found. Please run enhancement first."
        )

@router.post("/documents/{document_id}/enhance/summary")
async def generate_executive_summary(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, str]:
    """
    Generate a professional executive summary for the document
    """
    # Get document and verify access
    document = await db.get(Document, document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    if document.status != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Document must be processed first"
        )
    
    # Get parsed data
    try:
        parsed_json = await storage_service.download_file(
            "parsed", 
            f"{document_id}/parsed_data.json"
        )
        parsed_data = json.loads(parsed_json.decode('utf-8'))
        
        # Generate summary
        assistant = DocumentAssistant()
        summary = await assistant._generate_executive_summary(parsed_data)
        
        return {
            "document_id": str(document_id),
            "executive_summary": summary
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate summary: {str(e)}"
        )

@router.post("/documents/{document_id}/enhance/glossary")
async def generate_glossary(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Generate a technical glossary for the document
    """
    # Get document and verify access
    document = await db.get(Document, document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    if document.status != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Document must be processed first"
        )
    
    # Get parsed data
    try:
        parsed_json = await storage_service.download_file(
            "parsed", 
            f"{document_id}/parsed_data.json"
        )
        parsed_data = json.loads(parsed_json.decode('utf-8'))
        
        # Generate glossary
        assistant = DocumentAssistant()
        glossary = await assistant._generate_glossary(parsed_data)
        
        return {
            "document_id": str(document_id),
            "glossary": glossary
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Glossary generation failed: {str(e)}"
        )

@router.post("/documents/{document_id}/enhance/structure")
async def suggest_document_structure(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Suggest an optimal documentation structure
    """
    # Get document and verify access
    document = await db.get(Document, document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    if document.status != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Document must be processed first"
        )
    
    # Get parsed data
    try:
        parsed_json = await storage_service.download_file(
            "parsed", 
            f"{document_id}/parsed_data.json"
        )
        parsed_data = json.loads(parsed_json.decode('utf-8'))
        
        # Suggest structure
        assistant = DocumentAssistant()
        sections = await assistant._suggest_documentation_structure(parsed_data)
        
        return {
            "document_id": str(document_id),
            "suggested_sections": sections
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Structure suggestion failed: {str(e)}"
        )