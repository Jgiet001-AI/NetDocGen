"""
API endpoints for handling supplemental information and interactive documentation assistance
"""
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Dict, Any, List, Optional
import json

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.document import Document
from app.services.storage import storage_service
from app.services.llm.document_assistant import DocumentAssistant

router = APIRouter()

@router.post("/documents/{document_id}/supplemental")
async def upload_supplemental_info(
    document_id: UUID,
    answers: str = Form(...),
    files: List[UploadFile] = File(default=None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload supplemental information for a document
    """
    # Get document
    from sqlalchemy import select
    result = await db.execute(select(Document).where(Document.id == document_id))
    document = result.scalar_one_or_none()
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    # Parse answers
    try:
        answers_data = json.loads(answers)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid answers format"
        )
    
    # Store supplemental files if provided
    file_paths = {}
    if files:
        for file in files:
            if file.filename:
                # Extract question ID from field name (e.g., "file_vlan_list")
                question_id = file.filename.replace("file_", "")
                
                # Upload to storage
                file_path = f"supplemental/{document_id}/{question_id}/{file.filename}"
                await storage_service.upload_file(
                    bucket_type="documents",
                    object_name=file_path,
                    file_data=file.file,
                    content_type=file.content_type
                )
                file_paths[question_id] = file_path
    
    # Store supplemental data
    supplemental_data = {
        "answers": answers_data,
        "file_paths": file_paths
    }
    
    # Save to storage
    from io import BytesIO
    supplemental_json = json.dumps(supplemental_data, indent=2)
    await storage_service.upload_file(
        bucket_type="documents",
        object_name=f"supplemental/{document_id}/data.json",
        file_data=BytesIO(supplemental_json.encode()),
        content_type="application/json"
    )
    
    return {
        "message": "Supplemental information saved successfully",
        "document_id": str(document_id)
    }

@router.post("/documents/{document_id}/analyze-missing")
async def analyze_missing_info(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Analyze parsed document to identify missing information
    """
    # Get document
    from sqlalchemy import select
    result = await db.execute(select(Document).where(Document.id == document_id))
    document = result.scalar_one_or_none()
    if not document or document.status != "completed":
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
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve parsed data: {str(e)}"
        )
    
    # Analyze what's missing
    missing_info = []
    
    # Check for network design pattern
    if not _detect_network_design(parsed_data):
        missing_info.append("network_design")
    
    # Check for VLAN information
    if not _has_vlan_info(parsed_data):
        missing_info.append("vlan_list")
    
    # Check for complete device details
    if _has_incomplete_devices(parsed_data):
        missing_info.append("device_details")
    
    # Check for port channels
    if _might_have_port_channels(parsed_data):
        missing_info.append("port_channels")
    
    # Check for site information
    if not _has_site_info(parsed_data):
        missing_info.append("site_details")
    
    return {
        "document_id": str(document_id),
        "missing_info": missing_info,
        "recommendations": _get_recommendations(missing_info)
    }

@router.post("/analysis/documents/{document_id}/suggest")
async def get_ai_suggestions(
    document_id: UUID,
    question_type: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Get AI suggestions for specific question types
    """
    # Get document and parsed data
    from sqlalchemy import select
    result = await db.execute(select(Document).where(Document.id == document_id))
    document = result.scalar_one_or_none()
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    try:
        parsed_json = await storage_service.download_file(
            "parsed",
            f"{document_id}/parsed_data.json"
        )
        parsed_data = json.loads(parsed_json.decode('utf-8'))
    except Exception:
        return {"suggestions": []}
    
    assistant = DocumentAssistant()
    suggestions = []
    
    if question_type == "network_design":
        # Analyze topology to suggest design pattern
        suggestions = await assistant._suggest_network_design(parsed_data)
    elif question_type == "device_details":
        # Suggest device models based on names
        suggestions = await assistant._suggest_device_models(parsed_data)
    
    return {"suggestions": suggestions}

@router.post("/analysis/documents/{document_id}/auto-analyze")
async def auto_analyze_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Auto-analyze document to pre-fill common questions
    """
    # Get document and parsed data
    from sqlalchemy import select
    result = await db.execute(select(Document).where(Document.id == document_id))
    document = result.scalar_one_or_none()
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    try:
        parsed_json = await storage_service.download_file(
            "parsed",
            f"{document_id}/parsed_data.json"
        )
        parsed_data = json.loads(parsed_json.decode('utf-8'))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve parsed data: {str(e)}"
        )
    
    # Analyze the document to pre-fill answers
    analysis = {}
    
    # Detect network design pattern
    shapes = parsed_data.get("shapes", [])
    connections = parsed_data.get("connections", [])
    device_names = [s.get("name", "").lower() for s in shapes]
    
    # Simple heuristics for network design detection
    if any("spine" in name or "leaf" in name for name in device_names):
        analysis["network_design"] = "spine_leaf"
    elif any("core" in name for name in device_names) and any("dist" in name or "distribution" in name for name in device_names):
        analysis["network_design"] = "three_tier"
    elif any("core" in name for name in device_names) and not any("dist" in name for name in device_names):
        analysis["network_design"] = "collapsed_core"
    elif any("hub" in name for name in device_names):
        analysis["network_design"] = "hub_spoke"
    elif any("dmz" in name or "firewall" in name for name in device_names):
        analysis["network_design"] = "dmz"
    elif len(shapes) > 10 and any("building" in name or "campus" in name for name in device_names):
        analysis["network_design"] = "campus"
    else:
        # Use AI for more complex analysis if needed
        analysis["network_design"] = "not_sure"
    
    # Detect if VLAN info exists
    has_vlan = _has_vlan_info(parsed_data)
    if has_vlan:
        # Extract VLAN info if found
        vlan_info = []
        for shape in shapes:
            props = shape.get("properties", {})
            for key, value in props.items():
                if "vlan" in key.lower():
                    vlan_info.append(f"{key}: {value}")
        if vlan_info:
            analysis["vlan_list"] = "\n".join(vlan_info)
    
    return {
        "analysis": analysis,
        "confidence": {
            "network_design": 0.8 if analysis.get("network_design") != "not_sure" else 0.3,
            "vlan_detection": 0.9 if has_vlan else 0.0
        }
    }

# Helper functions
def _detect_network_design(parsed_data: Dict[str, Any]) -> bool:
    """Check if network design pattern can be detected"""
    # Simple heuristic - could be enhanced with ML
    shapes = parsed_data.get("shapes", [])
    connections = parsed_data.get("connections", [])
    
    if not shapes or not connections:
        return False
    
    # Look for keywords in device names/types
    device_names = [s.get("name", "").lower() for s in shapes]
    has_core = any("core" in name for name in device_names)
    has_dist = any("dist" in name or "distribution" in name for name in device_names)
    has_access = any("access" in name for name in device_names)
    
    return has_core or has_dist or has_access

def _has_vlan_info(parsed_data: Dict[str, Any]) -> bool:
    """Check if VLAN information is present"""
    shapes = parsed_data.get("shapes", [])
    connections = parsed_data.get("connections", [])
    
    # Check shape properties
    for shape in shapes:
        props = shape.get("properties", {})
        if any("vlan" in str(v).lower() for v in props.values()):
            return True
    
    # Check connection properties
    for conn in connections:
        props = conn.get("properties", {})
        if any("vlan" in str(v).lower() for v in props.values()):
            return True
    
    return False

def _has_incomplete_devices(parsed_data: Dict[str, Any]) -> bool:
    """Check if any devices are missing key information"""
    shapes = parsed_data.get("shapes", [])
    
    for shape in shapes:
        # Check if missing model info
        props = shape.get("properties", {})
        has_model = any(key in props for key in ["model", "device_model", "hardware"])
        has_ip = any(key in props for key in ["ip", "ip_address", "management_ip"])
        
        if not has_model or not has_ip:
            return True
    
    return False

def _might_have_port_channels(parsed_data: Dict[str, Any]) -> bool:
    """Check if the diagram might have port channels"""
    connections = parsed_data.get("connections", [])
    
    # Look for multiple connections between same devices
    connection_pairs = {}
    for conn in connections:
        pair = (conn.get("source_id"), conn.get("target_id"))
        reverse_pair = (conn.get("target_id"), conn.get("source_id"))
        
        if pair in connection_pairs or reverse_pair in connection_pairs:
            return True
        connection_pairs[pair] = True
    
    return False

def _has_site_info(parsed_data: Dict[str, Any]) -> bool:
    """Check if site/location information is present"""
    shapes = parsed_data.get("shapes", [])
    
    for shape in shapes:
        props = shape.get("properties", {})
        if any(key in props for key in ["site", "location", "building", "floor", "rack"]):
            return True
    
    return False

def _get_recommendations(missing_info: List[str]) -> List[str]:
    """Get recommendations based on missing information"""
    recommendations = []
    
    if "network_design" in missing_info:
        recommendations.append("Identifying the network design pattern helps organize documentation")
    
    if "vlan_list" in missing_info:
        recommendations.append("VLAN information is crucial for understanding network segmentation")
    
    if "device_details" in missing_info:
        recommendations.append("Complete device information improves documentation accuracy")
    
    return recommendations