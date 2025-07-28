from sqlalchemy import Column, String, DateTime, Text, Boolean, JSON, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

from .base import Base

class TemplateType(str, enum.Enum):
    NETWORK_DOCUMENTATION = "network_documentation"
    EXECUTIVE_SUMMARY = "executive_summary"
    TECHNICAL_REPORT = "technical_report"
    CUSTOM = "custom"

class OutputFormat(str, enum.Enum):
    HTML = "html"
    PDF = "pdf"
    DOCX = "docx"
    MARKDOWN = "markdown"

class DocumentTemplate(Base):
    __tablename__ = "document_templates"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    template_type = Column(Enum(TemplateType), default=TemplateType.NETWORK_DOCUMENTATION)
    
    # Organization Association
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    
    # Template Content
    html_template = Column(Text)  # Jinja2 HTML template
    css_styles = Column(Text)  # Custom CSS styles
    header_template = Column(Text)  # Header template
    footer_template = Column(Text)  # Footer template
    cover_page_template = Column(Text)  # Cover page template
    
    # Template Configuration
    supported_formats = Column(JSON, default=["html", "pdf"])  # List of supported output formats
    template_variables = Column(JSON)  # Available template variables and their descriptions
    section_config = Column(JSON)  # Configuration for document sections
    
    # Styling Configuration
    page_margins = Column(JSON, default={"top": "1in", "right": "1in", "bottom": "1in", "left": "1in"})
    font_config = Column(JSON)  # Font family, sizes, weights for different elements
    color_scheme = Column(JSON)  # Color scheme configuration
    logo_config = Column(JSON)  # Logo placement and sizing configuration
    
    # Template Metadata
    version = Column(String(20), default="1.0")
    author = Column(String(255))
    is_default = Column(Boolean, default=False)
    is_system_template = Column(Boolean, default=False)  # System vs user-created templates
    
    # Usage and Status
    usage_count = Column(JSON, default=0)  # Number of times template has been used
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization", back_populates="document_templates")
    documents = relationship("Document", back_populates="template")
    
    def __repr__(self):
        return f"<DocumentTemplate(name='{self.name}', type='{self.template_type}')>"