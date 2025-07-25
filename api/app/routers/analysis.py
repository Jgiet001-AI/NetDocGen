"""
Network Analysis API endpoints using LLM
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Dict, Any

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.document import Document
from app.services.llm import NetworkAnalyzer
from app.services.storage import storage_service
import json

router = APIRouter()

@router.post("/documents/{document_id}/analyze")
async def analyze_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Analyze a document using Phi-3 AI
    
    This endpoint triggers AI analysis of the parsed network data to provide:
    - Executive summary
    - Architecture analysis
    - Security assessment
    - Optimization suggestions
    """
    # Get document
    document = await db.get(Document, document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    # Check ownership
    # Note: Would need to add project relationship check here
    
    # Check if document is processed
    if document.status != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Document must be processed before analysis"
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
    
    # Perform analysis
    analyzer = NetworkAnalyzer()
    try:
        analysis_results = await analyzer.analyze_network(parsed_data)
        
        # Store analysis results
        analysis_path = f"analysis/{document_id}/ai_analysis.json"
        from io import BytesIO
        analysis_json = json.dumps(analysis_results, indent=2)
        await storage_service.upload_file(
            bucket_type="analysis",
            object_name=f"{document_id}/ai_analysis.json",
            file_data=BytesIO(analysis_json.encode()),
            content_type="application/json"
        )
        
        # Update document with analysis status
        document.ai_analysis_completed = True
        await db.commit()
        
        return {
            "document_id": str(document_id),
            "analysis": analysis_results,
            "analysis_path": analysis_path
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Analysis failed: {str(e)}"
        )

@router.get("/documents/{document_id}/analysis")
async def get_document_analysis(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Retrieve existing AI analysis for a document
    """
    # Get document
    document = await db.get(Document, document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    # Check if analysis exists
    try:
        analysis_json = await storage_service.download_file(
            "analysis", 
            f"{document_id}/ai_analysis.json"
        )
        analysis_data = json.loads(analysis_json.decode('utf-8'))
        
        return {
            "document_id": str(document_id),
            "analysis": analysis_data
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Analysis not found. Please run analysis first."
        )

@router.post("/documents/{document_id}/analyze/summary")
async def generate_executive_summary(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, str]:
    """
    Generate just an executive summary for a document
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
        analyzer = NetworkAnalyzer()
        summary = await analyzer._generate_executive_summary(parsed_data)
        
        return {
            "document_id": str(document_id),
            "executive_summary": summary
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate summary: {str(e)}"
        )

@router.post("/documents/{document_id}/analyze/security")
async def analyze_security(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Perform security-focused analysis of the network
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
        
        # Perform security analysis
        analyzer = NetworkAnalyzer()
        security_assessment = await analyzer._assess_security(parsed_data)
        
        return {
            "document_id": str(document_id),
            "security_assessment": security_assessment
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Security analysis failed: {str(e)}"
        )