from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any, List
from datetime import datetime
from uuid import UUID
from app.models.document import DocumentStatus

# Base schemas
class DocumentBase(BaseModel):
    filename: str = Field(..., min_length=1, max_length=255)

class DocumentCreate(BaseModel):
    project_id: UUID

class DocumentUpdate(BaseModel):
    status: Optional[DocumentStatus] = None
    error_message: Optional[str] = None
    parsed_data_path: Optional[str] = None
    shape_count: Optional[int] = None
    connection_count: Optional[int] = None
    page_count: Optional[int] = None
    generated_files: Optional[Dict[str, str]] = None

# Response schemas
class DocumentSummary(BaseModel):
    id: UUID
    filename: str
    status: DocumentStatus
    uploaded_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class Document(DocumentBase):
    id: UUID
    project_id: UUID
    original_filename: str
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    content_type: Optional[str] = None
    status: DocumentStatus
    error_message: Optional[str] = None
    shape_count: Optional[int] = None
    connection_count: Optional[int] = None
    page_count: Optional[int] = None
    generated_files: Optional[Dict[str, str]] = None
    uploaded_by: UUID
    uploaded_at: datetime
    parsed_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)

class DocumentUploadResponse(BaseModel):
    id: UUID
    filename: str
    status: DocumentStatus
    message: str
    
class DocumentGenerateRequest(BaseModel):
    formats: List[str] = Field(default=["html"], description="Output formats: html, pdf, docx, markdown")
    
class DocumentGenerateResponse(BaseModel):
    document_id: UUID
    status: str
    message: str
    generated_files: Optional[Dict[str, str]] = None

class ParsedData(BaseModel):
    shapes: List[Dict[str, Any]]
    connections: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    page_count: int