"""
Collaboration models for sharing projects and documents
"""
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum as SQLEnum, Table, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from enum import Enum

from app.database import Base

# Association table for project collaborators
project_collaborators = Table(
    'project_collaborators',
    Base.metadata,
    Column('project_id', UUID(as_uuid=True), ForeignKey('projects.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('role', String, nullable=False, default='viewer'),
    Column('added_at', DateTime, default=datetime.utcnow),
    Column('added_by', UUID(as_uuid=True), ForeignKey('users.id'))
)

class SharePermission(str, Enum):
    VIEW = "view"
    EDIT = "edit"
    ADMIN = "admin"

class ShareLink(Base):
    """Share links for projects and documents"""
    __tablename__ = "share_links"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    token = Column(String, unique=True, nullable=False, index=True)
    
    # Resource being shared
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=True)
    
    # Share settings
    permission = Column(SQLEnum(SharePermission), default=SharePermission.VIEW)
    expires_at = Column(DateTime, nullable=True)
    max_uses = Column(Integer, nullable=True)
    use_count = Column(Integer, default=0)
    password_hash = Column(String, nullable=True)
    
    # Metadata
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_accessed = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    creator = relationship("User", back_populates="share_links")
    project = relationship("Project", back_populates="share_links")
    document = relationship("Document", back_populates="share_links")
    
    def is_valid(self) -> bool:
        """Check if share link is still valid"""
        if not self.is_active:
            return False
        if self.expires_at and datetime.utcnow() > self.expires_at:
            return False
        if self.max_uses and self.use_count >= self.max_uses:
            return False
        return True

class Comment(Base):
    """Comments on documents and projects"""
    __tablename__ = "comments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    content = Column(String, nullable=False)
    
    # Parent resource
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=True)
    
    # Threading
    parent_id = Column(UUID(as_uuid=True), ForeignKey("comments.id"), nullable=True)
    
    # Metadata
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
    
    # Relationships
    user = relationship("User", back_populates="comments")
    project = relationship("Project", back_populates="comments")
    document = relationship("Document", back_populates="comments")
    parent = relationship("Comment", remote_side=[id], backref="replies")

class Activity(Base):
    """Activity log for projects and documents"""
    __tablename__ = "activities"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    action = Column(String, nullable=False)  # created, updated, deleted, shared, commented
    description = Column(String, nullable=True)
    
    # Resource
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=True)
    
    # Metadata
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    metadata = Column(JSON, nullable=True)  # Additional context
    
    # Relationships
    user = relationship("User", back_populates="activities")
    project = relationship("Project", back_populates="activities")
    document = relationship("Document", back_populates="activities")