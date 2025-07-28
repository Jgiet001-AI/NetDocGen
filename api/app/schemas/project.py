from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID
from app.models.project import ProjectStatus

# Base schemas
class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    
    # Customer Information
    customer_name: Optional[str] = None
    customer_organization: Optional[str] = None
    customer_contact_name: Optional[str] = None
    customer_contact_email: Optional[str] = None
    customer_contact_phone: Optional[str] = None
    
    # Project Details
    project_code: Optional[str] = None
    project_manager: Optional[str] = None
    contract_number: Optional[str] = None
    po_number: Optional[str] = None
    
    # Project Metadata
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    budget: Optional[str] = None
    priority: Optional[str] = "medium"
    
    # Custom Fields
    custom_fields: Optional[Dict[str, Any]] = None
    project_settings: Optional[Dict[str, Any]] = None

class ProjectCreate(ProjectBase):
    organization_id: Optional[UUID] = None

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None
    
    # Customer Information
    customer_name: Optional[str] = None
    customer_organization: Optional[str] = None
    customer_contact_name: Optional[str] = None
    customer_contact_email: Optional[str] = None
    customer_contact_phone: Optional[str] = None
    
    # Project Details
    project_code: Optional[str] = None
    project_manager: Optional[str] = None
    contract_number: Optional[str] = None
    po_number: Optional[str] = None
    
    # Project Metadata
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    budget: Optional[str] = None
    priority: Optional[str] = None
    
    # Custom Fields
    custom_fields: Optional[Dict[str, Any]] = None
    project_settings: Optional[Dict[str, Any]] = None

# Response schemas
class ProjectSummary(BaseModel):
    id: UUID
    name: str
    status: ProjectStatus
    customer_name: Optional[str] = None
    project_code: Optional[str] = None
    document_count: int = 0
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class Project(ProjectBase):
    id: UUID
    status: ProjectStatus
    owner_id: UUID
    organization_id: Optional[UUID] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)

class ProjectWithDocuments(Project):
    documents: List["DocumentSummary"] = []
    
    model_config = ConfigDict(from_attributes=True)

# Import at the end to avoid circular imports
from .document import DocumentSummary
ProjectWithDocuments.model_rebuild()