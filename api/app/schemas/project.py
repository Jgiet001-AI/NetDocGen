from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from app.models.project import ProjectStatus

# Base schemas
class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None

# Response schemas
class ProjectSummary(BaseModel):
    id: UUID
    name: str
    status: ProjectStatus
    document_count: int = 0
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class Project(ProjectBase):
    id: UUID
    status: ProjectStatus
    owner_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)

class ProjectWithDocuments(Project):
    documents: List["DocumentSummary"] = []
    
    model_config = ConfigDict(from_attributes=True)

# Import at the end to avoid circular imports
from .document import DocumentSummary
ProjectWithDocuments.model_rebuild()