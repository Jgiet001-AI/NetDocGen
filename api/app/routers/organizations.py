"""
Organization management API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from typing import List, Optional
import json

from app.database import get_db
from app.dependencies import get_current_user
from app.models import User, Organization, DocumentTemplate
from app.services.storage import storage_service
from pydantic import BaseModel

router = APIRouter()

# Pydantic models for API requests/responses
class OrganizationBase(BaseModel):
    name: str
    display_name: Optional[str] = None
    description: Optional[str] = None
    primary_contact: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    primary_color: Optional[str] = "#1e3c72"
    secondary_color: Optional[str] = "#2a5298"
    accent_color: Optional[str] = "#4CAF50"
    default_font_family: Optional[str] = "Arial"
    default_font_size: Optional[str] = "14px"
    letterhead_html: Optional[str] = None
    footer_html: Optional[str] = None
    default_template_style: Optional[str] = "professional"
    document_numbering_format: Optional[str] = "DOC-{year}-{seq:04d}"

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    primary_contact: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    primary_color: Optional[str] = None
    secondary_color: Optional[str] = None
    accent_color: Optional[str] = None
    default_font_family: Optional[str] = None
    default_font_size: Optional[str] = None
    letterhead_html: Optional[str] = None
    footer_html: Optional[str] = None
    default_template_style: Optional[str] = None
    document_numbering_format: Optional[str] = None

class OrganizationResponse(OrganizationBase):
    id: UUID
    logo_url: Optional[str] = None
    is_active: bool
    created_at: str
    updated_at: Optional[str] = None
    user_count: Optional[int] = 0
    project_count: Optional[int] = 0
    template_count: Optional[int] = 0

    class Config:
        from_attributes = True

@router.get("", response_model=List[OrganizationResponse])
async def list_organizations(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get list of organizations (admin only or user's own organization)
    """
    if current_user.is_admin:
        # Admin can see all organizations
        result = await db.execute(
            select(Organization)
            .offset(skip)
            .limit(limit)
            .order_by(Organization.created_at.desc())
        )
        organizations = result.scalars().all()
    else:
        # Regular users can only see their own organization
        if not current_user.organization_id:
            return []
        
        result = await db.execute(
            select(Organization)
            .where(Organization.id == current_user.organization_id)
        )
        organizations = result.scalars().all()
    
    return organizations

@router.post("", response_model=OrganizationResponse)
async def create_organization(
    organization: OrganizationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create new organization (admin only)
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only administrators can create organizations"
        )
    
    db_organization = Organization(**organization.dict())
    db.add(db_organization)
    await db.commit()
    await db.refresh(db_organization)
    
    return db_organization

@router.get("/{organization_id}", response_model=OrganizationResponse)
async def get_organization(
    organization_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get organization by ID
    """
    # Check permissions
    if not current_user.is_admin and current_user.organization_id != organization_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this organization"
        )
    
    result = await db.execute(
        select(Organization).where(Organization.id == organization_id)
    )
    organization = result.scalar_one_or_none()
    
    if not organization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found"
        )
    
    return organization

@router.put("/{organization_id}", response_model=OrganizationResponse)
async def update_organization(
    organization_id: UUID,
    organization_update: OrganizationUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update organization
    """
    # Check permissions
    if not current_user.is_admin and current_user.organization_id != organization_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this organization"
        )
    
    result = await db.execute(
        select(Organization).where(Organization.id == organization_id)
    )
    db_organization = result.scalar_one_or_none()
    
    if not db_organization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found"
        )
    
    # Update fields
    update_data = organization_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_organization, field, value)
    
    await db.commit()
    await db.refresh(db_organization)
    
    return db_organization

@router.post("/{organization_id}/logo", response_model=dict)
async def upload_organization_logo(
    organization_id: UUID,
    logo: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload organization logo
    """
    # Check permissions
    if not current_user.is_admin and current_user.organization_id != organization_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this organization"
        )
    
    # Validate file type
    if not logo.content_type.startswith('image/'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only image files are allowed"
        )
    
    # Get organization
    result = await db.execute(
        select(Organization).where(Organization.id == organization_id)
    )
    db_organization = result.scalar_one_or_none()
    
    if not db_organization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found"
        )
    
    # Upload logo to storage
    object_name = f"organizations/{organization_id}/logo/{logo.filename}"
    await storage_service.upload_file(
        bucket_type="documents",
        object_name=object_name,
        file_data=logo.file,
        content_type=logo.content_type
    )
    
    # Update organization with logo URL
    logo_url = f"/api/storage/documents/{object_name}"
    db_organization.logo_url = logo_url
    
    await db.commit()
    
    return {
        "message": "Logo uploaded successfully",
        "logo_url": logo_url
    }

@router.delete("/{organization_id}")
async def delete_organization(
    organization_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete organization (admin only)
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only administrators can delete organizations"
        )
    
    result = await db.execute(
        select(Organization).where(Organization.id == organization_id)
    )
    db_organization = result.scalar_one_or_none()
    
    if not db_organization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found"
        )
    
    # Soft delete by setting is_active to False
    db_organization.is_active = False
    await db.commit()
    
    return {"message": "Organization deleted successfully"}

@router.get("/current", response_model=Optional[OrganizationResponse])
async def get_current_user_organization(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get current user's organization
    """
    if not current_user.organization_id:
        return None
    
    result = await db.execute(
        select(Organization).where(Organization.id == current_user.organization_id)
    )
    organization = result.scalar_one_or_none()
    
    return organization