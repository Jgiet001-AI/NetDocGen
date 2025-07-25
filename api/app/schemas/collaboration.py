"""
Pydantic schemas for collaboration features
"""
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from enum import Enum

class SharePermission(str, Enum):
    VIEW = "view"
    EDIT = "edit"
    ADMIN = "admin"

# Share Link Schemas
class ShareLinkBase(BaseModel):
    permission: SharePermission = SharePermission.VIEW
    expires_at: Optional[datetime] = None
    max_uses: Optional[int] = None
    password: Optional[str] = None

class ShareLinkCreate(ShareLinkBase):
    project_id: Optional[UUID] = None
    document_id: Optional[UUID] = None
    
    @validator('document_id')
    def validate_resource(cls, v, values):
        if not v and not values.get('project_id'):
            raise ValueError('Either project_id or document_id must be provided')
        if v and values.get('project_id'):
            raise ValueError('Only one of project_id or document_id can be provided')
        return v

class ShareLinkResponse(ShareLinkBase):
    id: UUID
    token: str
    project_id: Optional[UUID]
    document_id: Optional[UUID]
    use_count: int
    created_by: UUID
    created_at: datetime
    last_accessed: Optional[datetime]
    is_active: bool
    share_url: str
    
    class Config:
        from_attributes = True

class ShareLinkAccess(BaseModel):
    password: Optional[str] = None

# Comment Schemas
class CommentBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=5000)

class CommentCreate(CommentBase):
    project_id: Optional[UUID] = None
    document_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    
    @validator('document_id')
    def validate_resource(cls, v, values):
        if not v and not values.get('project_id'):
            raise ValueError('Either project_id or document_id must be provided')
        return v

class CommentUpdate(BaseModel):
    content: str = Field(..., min_length=1, max_length=5000)

class CommentResponse(CommentBase):
    id: UUID
    project_id: Optional[UUID]
    document_id: Optional[UUID]
    parent_id: Optional[UUID]
    user_id: UUID
    user_name: str
    created_at: datetime
    updated_at: datetime
    is_deleted: bool
    replies: List['CommentResponse'] = []
    
    class Config:
        from_attributes = True

# Activity Schemas
class ActivityResponse(BaseModel):
    id: UUID
    action: str
    description: Optional[str]
    project_id: Optional[UUID]
    document_id: Optional[UUID]
    user_id: UUID
    user_name: str
    timestamp: datetime
    metadata: Optional[dict]
    
    class Config:
        from_attributes = True

# Collaborator Schemas
class CollaboratorAdd(BaseModel):
    user_email: str
    role: str = "viewer"

class CollaboratorResponse(BaseModel):
    user_id: UUID
    email: str
    full_name: Optional[str]
    role: str
    added_at: datetime
    added_by: UUID
    
    class Config:
        from_attributes = True

# Update forward references
CommentResponse.model_rebuild()