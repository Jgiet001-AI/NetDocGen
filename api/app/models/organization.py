from sqlalchemy import Column, String, DateTime, Text, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from .base import Base

class Organization(Base):
    __tablename__ = "organizations"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255))  # For document headers
    description = Column(Text)
    
    # Contact Information
    primary_contact = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    website = Column(String(255))
    
    # Address Information
    address_line1 = Column(String(255))
    address_line2 = Column(String(255))
    city = Column(String(100))
    state = Column(String(100))
    postal_code = Column(String(20))
    country = Column(String(100))
    
    # Branding Configuration
    logo_url = Column(String(500))  # URL to organization logo
    primary_color = Column(String(7), default="#1e3c72")  # Hex color
    secondary_color = Column(String(7), default="#2a5298")  # Hex color
    accent_color = Column(String(7), default="#4CAF50")  # Hex color
    
    # Document Settings
    default_font_family = Column(String(100), default="Arial")
    default_font_size = Column(String(10), default="14px")
    letterhead_html = Column(Text)  # Custom HTML letterhead
    footer_html = Column(Text)  # Custom HTML footer
    
    # Template Preferences
    default_template_style = Column(String(50), default="professional")
    document_numbering_format = Column(String(100), default="DOC-{year}-{seq:04d}")
    
    # Metadata and Configuration
    custom_fields = Column(JSON)  # Additional configurable fields
    branding_config = Column(JSON)  # Advanced branding settings
    
    # Status and Audit
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    users = relationship("User", back_populates="organization")
    projects = relationship("Project", back_populates="organization")
    document_templates = relationship("DocumentTemplate", back_populates="organization")