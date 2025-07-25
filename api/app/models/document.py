from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Enum, JSON, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

from .base import Base

class DocumentStatus(str, enum.Enum):
    UPLOADED = "uploaded"
    PARSING = "parsing"
    PARSED = "parsed"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    original_filename = Column(String(255), nullable=False)
    file_path = Column(String(500))  # Path in MinIO
    file_size = Column(Integer)  # Size in bytes
    content_type = Column(String(100))
    status = Column(Enum(DocumentStatus), default=DocumentStatus.UPLOADED)
    error_message = Column(Text)
    
    # Parsed data from Visio
    parsed_data_path = Column(String(500))  # Path to parsed JSON in MinIO
    shape_count = Column(Integer)
    connection_count = Column(Integer)
    page_count = Column(Integer)
    
    # Generated documentation paths
    generated_files = Column(JSON)  # {"html": "path", "pdf": "path", etc.}
    
    uploaded_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    parsed_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    
    # AI Analysis
    ai_analysis_completed = Column(Boolean, default=False)
    
    # Relationships
    project = relationship("Project", back_populates="documents")
    uploaded_by_user = relationship("User")