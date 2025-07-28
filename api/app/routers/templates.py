"""
Document template management API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from typing import List, Optional, Dict, Any
import json

from app.database import get_db
from app.dependencies import get_current_user
from app.models import User, Organization, DocumentTemplate, TemplateType, OutputFormat
from pydantic import BaseModel

router = APIRouter()

# Pydantic models for API requests/responses
class DocumentTemplateBase(BaseModel):
    name: str
    description: Optional[str] = None
    template_type: TemplateType = TemplateType.NETWORK_DOCUMENTATION
    html_template: Optional[str] = None
    css_styles: Optional[str] = None
    header_template: Optional[str] = None
    footer_template: Optional[str] = None
    cover_page_template: Optional[str] = None
    supported_formats: Optional[List[str]] = ["html", "pdf"]
    template_variables: Optional[Dict[str, Any]] = None
    section_config: Optional[Dict[str, Any]] = None
    page_margins: Optional[Dict[str, str]] = {"top": "1in", "right": "1in", "bottom": "1in", "left": "1in"}
    font_config: Optional[Dict[str, Any]] = None
    color_scheme: Optional[Dict[str, str]] = None
    logo_config: Optional[Dict[str, Any]] = None
    version: Optional[str] = "1.0"
    author: Optional[str] = None
    is_default: Optional[bool] = False

class DocumentTemplateCreate(DocumentTemplateBase):
    organization_id: UUID

class DocumentTemplateUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    template_type: Optional[TemplateType] = None
    html_template: Optional[str] = None
    css_styles: Optional[str] = None
    header_template: Optional[str] = None
    footer_template: Optional[str] = None
    cover_page_template: Optional[str] = None
    supported_formats: Optional[List[str]] = None
    template_variables: Optional[Dict[str, Any]] = None
    section_config: Optional[Dict[str, Any]] = None
    page_margins: Optional[Dict[str, str]] = None
    font_config: Optional[Dict[str, Any]] = None
    color_scheme: Optional[Dict[str, str]] = None
    logo_config: Optional[Dict[str, Any]] = None
    version: Optional[str] = None
    author: Optional[str] = None
    is_default: Optional[bool] = None

class DocumentTemplateResponse(DocumentTemplateBase):
    id: UUID
    organization_id: UUID
    usage_count: int
    is_system_template: bool
    is_active: bool
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

@router.get("", response_model=List[DocumentTemplateResponse])
async def list_templates(
    organization_id: Optional[UUID] = None,
    template_type: Optional[TemplateType] = None,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get list of document templates
    """
    query = select(DocumentTemplate).where(DocumentTemplate.is_active == True)
    
    # Filter by organization if specified or user's organization
    if organization_id:
        if not current_user.is_admin and current_user.organization_id != organization_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied to organization templates"
            )
        query = query.where(DocumentTemplate.organization_id == organization_id)
    elif current_user.organization_id:
        # Show user's organization templates + system templates
        query = query.where(
            (DocumentTemplate.organization_id == current_user.organization_id) |
            (DocumentTemplate.is_system_template == True)
        )
    else:
        # Show only system templates if user has no organization
        query = query.where(DocumentTemplate.is_system_template == True)
    
    # Filter by template type if specified
    if template_type:
        query = query.where(DocumentTemplate.template_type == template_type)
    
    query = query.offset(skip).limit(limit).order_by(DocumentTemplate.created_at.desc())
    
    result = await db.execute(query)
    templates = result.scalars().all()
    
    return templates

@router.post("", response_model=DocumentTemplateResponse)
async def create_template(
    template: DocumentTemplateCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create new document template
    """
    # Check permissions
    if not current_user.is_admin and current_user.organization_id != template.organization_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Can only create templates for your organization"
        )
    
    # Verify organization exists
    result = await db.execute(
        select(Organization).where(Organization.id == template.organization_id)
    )
    organization = result.scalar_one_or_none()
    
    if not organization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found"
        )
    
    # Create template
    template_data = template.dict()
    template_data['author'] = current_user.full_name or current_user.username
    
    db_template = DocumentTemplate(**template_data)
    db.add(db_template)
    await db.commit()
    await db.refresh(db_template)
    
    return db_template

@router.get("/{template_id}", response_model=DocumentTemplateResponse)
async def get_template(
    template_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get document template by ID
    """
    result = await db.execute(
        select(DocumentTemplate).where(DocumentTemplate.id == template_id)
    )
    template = result.scalar_one_or_none()
    
    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found"
        )
    
    # Check permissions
    if not template.is_system_template:
        if not current_user.is_admin and current_user.organization_id != template.organization_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied to this template"
            )
    
    return template

@router.put("/{template_id}", response_model=DocumentTemplateResponse)
async def update_template(
    template_id: UUID,
    template_update: DocumentTemplateUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update document template
    """
    result = await db.execute(
        select(DocumentTemplate).where(DocumentTemplate.id == template_id)
    )
    db_template = result.scalar_one_or_none()
    
    if not db_template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found"
        )
    
    # Check permissions
    if db_template.is_system_template and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot modify system templates"
        )
    
    if not db_template.is_system_template:
        if not current_user.is_admin and current_user.organization_id != db_template.organization_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied to this template"
            )
    
    # Update fields
    update_data = template_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_template, field, value)
    
    await db.commit()
    await db.refresh(db_template)
    
    return db_template

@router.delete("/{template_id}")
async def delete_template(
    template_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete document template
    """
    result = await db.execute(
        select(DocumentTemplate).where(DocumentTemplate.id == template_id)
    )
    db_template = result.scalar_one_or_none()
    
    if not db_template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found"
        )
    
    # Check permissions
    if db_template.is_system_template:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot delete system templates"
        )
    
    if not current_user.is_admin and current_user.organization_id != db_template.organization_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this template"
        )
    
    # Soft delete by setting is_active to False
    db_template.is_active = False
    await db.commit()
    
    return {"message": "Template deleted successfully"}

@router.post("/{template_id}/clone", response_model=DocumentTemplateResponse)
async def clone_template(
    template_id: UUID,
    name: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Clone a template to user's organization
    """
    if not current_user.organization_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User must belong to an organization to clone templates"
        )
    
    # Get original template
    result = await db.execute(
        select(DocumentTemplate).where(DocumentTemplate.id == template_id)
    )
    original_template = result.scalar_one_or_none()
    
    if not original_template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found"
        )
    
    # Check if user can access the template
    if not original_template.is_system_template:
        if not current_user.is_admin and current_user.organization_id != original_template.organization_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied to this template"
            )
    
    # Create cloned template
    template_data = {
        'name': name,
        'description': f"Cloned from {original_template.name}",
        'template_type': original_template.template_type,
        'organization_id': current_user.organization_id,
        'html_template': original_template.html_template,
        'css_styles': original_template.css_styles,
        'header_template': original_template.header_template,
        'footer_template': original_template.footer_template,
        'cover_page_template': original_template.cover_page_template,
        'supported_formats': original_template.supported_formats,
        'template_variables': original_template.template_variables,
        'section_config': original_template.section_config,
        'page_margins': original_template.page_margins,
        'font_config': original_template.font_config,
        'color_scheme': original_template.color_scheme,
        'logo_config': original_template.logo_config,
        'author': current_user.full_name or current_user.username,
        'is_system_template': False,
        'is_default': False
    }
    
    db_template = DocumentTemplate(**template_data)
    db.add(db_template)
    await db.commit()
    await db.refresh(db_template)
    
    return db_template

@router.get("/{template_id}/preview")
async def preview_template(
    template_id: UUID,
    sample_data: Optional[Dict[str, Any]] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Generate preview of template with sample data
    """
    result = await db.execute(
        select(DocumentTemplate).where(DocumentTemplate.id == template_id)
    )
    template = result.scalar_one_or_none()
    
    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found"
        )
    
    # Check permissions
    if not template.is_system_template:
        if not current_user.is_admin and current_user.organization_id != template.organization_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied to this template"
            )
    
    # Use sample data or default preview data
    if not sample_data:
        sample_data = {
            "title": "Sample Network Documentation",
            "project_name": "Sample Project",
            "customer_name": "Sample Customer",
            "generated_date": "2025-07-25",
            "shapes": [
                {"name": "Core-Switch-01", "type": "switch", "connections_count": 4},
                {"name": "Firewall-01", "type": "firewall", "connections_count": 2}
            ],
            "connections": [
                {"source_name": "Core-Switch-01", "target_name": "Firewall-01", "connection_type": "ethernet"}
            ]
        }
    
    # Generate preview (simplified HTML rendering)
    from jinja2 import Template
    
    try:
        if template.html_template:
            jinja_template = Template(template.html_template)
            preview_html = jinja_template.render(**sample_data)
            
            return {
                "preview_html": preview_html,
                "css_styles": template.css_styles,
                "template_variables": template.template_variables
            }
        else:
            return {
                "preview_html": "<p>No template content available</p>",
                "message": "Template has no HTML content"
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error rendering template: {str(e)}"
        )