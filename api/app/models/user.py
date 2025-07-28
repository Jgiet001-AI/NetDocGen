from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    # Organization Association
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    default_template_id = Column(UUID(as_uuid=True), ForeignKey("document_templates.id"))
    
    # User Preferences
    role = Column(String(50), default="user")  # user, admin, manager
    timezone = Column(String(50), default="UTC")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization", back_populates="users")
    default_template = relationship("DocumentTemplate", foreign_keys=[default_template_id])
    projects = relationship("Project", back_populates="owner", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="user")
    share_links = relationship("ShareLink", back_populates="creator")
    comments = relationship("Comment", back_populates="user")
    activities = relationship("Activity", back_populates="user")