from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

from .base import Base

class ProjectStatus(str, enum.Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.ACTIVE)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    
    # Customer Information
    customer_name = Column(String(255))
    customer_organization = Column(String(255))
    customer_contact_name = Column(String(255))
    customer_contact_email = Column(String(255))
    customer_contact_phone = Column(String(50))
    
    # Project Details
    project_code = Column(String(100))  # Custom project reference code
    project_manager = Column(String(255))
    contract_number = Column(String(100))
    po_number = Column(String(100))
    
    # Project Metadata
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    budget = Column(String(50))  # Stored as string to handle currencies
    priority = Column(String(20), default="medium")  # low, medium, high, critical
    
    # Custom Fields and Configuration
    custom_fields = Column(JSON)  # Additional configurable fields
    project_settings = Column(JSON)  # Project-specific settings
    
    # Audit Fields
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    owner = relationship("User", back_populates="projects")
    organization = relationship("Organization", back_populates="projects")
    documents = relationship("Document", back_populates="project", cascade="all, delete-orphan")
    share_links = relationship("ShareLink", back_populates="project")
    comments = relationship("Comment", back_populates="project")
    activities = relationship("Activity", back_populates="project")