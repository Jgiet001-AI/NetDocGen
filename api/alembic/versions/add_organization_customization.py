"""Add organization and customization models

Revision ID: add_organization_customization
Revises: de1689ae5d8c
Create Date: 2025-07-25 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'add_organization_customization'
down_revision = 'add_unique_project_name'
branch_labels = None
depends_on = None


def upgrade():
    # Create organizations table
    op.create_table('organizations',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('display_name', sa.String(length=255), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('primary_contact', sa.String(length=255), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('phone', sa.String(length=50), nullable=True),
        sa.Column('website', sa.String(length=255), nullable=True),
        sa.Column('address_line1', sa.String(length=255), nullable=True),
        sa.Column('address_line2', sa.String(length=255), nullable=True),
        sa.Column('city', sa.String(length=100), nullable=True),
        sa.Column('state', sa.String(length=100), nullable=True),
        sa.Column('postal_code', sa.String(length=20), nullable=True),
        sa.Column('country', sa.String(length=100), nullable=True),
        sa.Column('logo_url', sa.String(length=500), nullable=True),
        sa.Column('primary_color', sa.String(length=7), nullable=True),
        sa.Column('secondary_color', sa.String(length=7), nullable=True),
        sa.Column('accent_color', sa.String(length=7), nullable=True),
        sa.Column('default_font_family', sa.String(length=100), nullable=True),
        sa.Column('default_font_size', sa.String(length=10), nullable=True),
        sa.Column('letterhead_html', sa.Text(), nullable=True),
        sa.Column('footer_html', sa.Text(), nullable=True),
        sa.Column('default_template_style', sa.String(length=50), nullable=True),
        sa.Column('document_numbering_format', sa.String(length=100), nullable=True),
        sa.Column('custom_fields', sa.JSON(), nullable=True),
        sa.Column('branding_config', sa.JSON(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create document_templates table
    op.create_table('document_templates',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('template_type', sa.Enum('NETWORK_DOCUMENTATION', 'EXECUTIVE_SUMMARY', 'TECHNICAL_REPORT', 'CUSTOM', name='templatetype'), nullable=True),
        sa.Column('organization_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('html_template', sa.Text(), nullable=True),
        sa.Column('css_styles', sa.Text(), nullable=True),
        sa.Column('header_template', sa.Text(), nullable=True),
        sa.Column('footer_template', sa.Text(), nullable=True),
        sa.Column('cover_page_template', sa.Text(), nullable=True),
        sa.Column('supported_formats', sa.JSON(), nullable=True),
        sa.Column('template_variables', sa.JSON(), nullable=True),
        sa.Column('section_config', sa.JSON(), nullable=True),
        sa.Column('page_margins', sa.JSON(), nullable=True),
        sa.Column('font_config', sa.JSON(), nullable=True),
        sa.Column('color_scheme', sa.JSON(), nullable=True),
        sa.Column('logo_config', sa.JSON(), nullable=True),
        sa.Column('version', sa.String(length=20), nullable=True),
        sa.Column('author', sa.String(length=255), nullable=True),
        sa.Column('is_default', sa.Boolean(), nullable=True),
        sa.Column('is_system_template', sa.Boolean(), nullable=True),
        sa.Column('usage_count', sa.JSON(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Add organization_id to users table
    op.add_column('users', sa.Column('organization_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('users', sa.Column('default_template_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('timezone', sa.String(length=50), nullable=True))
    
    op.create_foreign_key(None, 'users', 'organizations', ['organization_id'], ['id'])
    op.create_foreign_key(None, 'users', 'document_templates', ['default_template_id'], ['id'])

    # Add customer and project fields to projects table
    op.add_column('projects', sa.Column('organization_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('projects', sa.Column('customer_name', sa.String(length=255), nullable=True))
    op.add_column('projects', sa.Column('customer_organization', sa.String(length=255), nullable=True))
    op.add_column('projects', sa.Column('customer_contact_name', sa.String(length=255), nullable=True))
    op.add_column('projects', sa.Column('customer_contact_email', sa.String(length=255), nullable=True))
    op.add_column('projects', sa.Column('customer_contact_phone', sa.String(length=50), nullable=True))
    op.add_column('projects', sa.Column('project_code', sa.String(length=100), nullable=True))
    op.add_column('projects', sa.Column('project_manager', sa.String(length=255), nullable=True))
    op.add_column('projects', sa.Column('contract_number', sa.String(length=100), nullable=True))
    op.add_column('projects', sa.Column('po_number', sa.String(length=100), nullable=True))
    op.add_column('projects', sa.Column('start_date', sa.DateTime(timezone=True), nullable=True))
    op.add_column('projects', sa.Column('end_date', sa.DateTime(timezone=True), nullable=True))
    op.add_column('projects', sa.Column('budget', sa.String(length=50), nullable=True))
    op.add_column('projects', sa.Column('priority', sa.String(length=20), nullable=True))
    op.add_column('projects', sa.Column('custom_fields', sa.JSON(), nullable=True))
    op.add_column('projects', sa.Column('project_settings', sa.JSON(), nullable=True))
    
    op.create_foreign_key(None, 'projects', 'organizations', ['organization_id'], ['id'])

    # Add template and branding fields to documents table
    op.add_column('documents', sa.Column('template_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('documents', sa.Column('branding_config', sa.JSON(), nullable=True))
    op.add_column('documents', sa.Column('generation_settings', sa.JSON(), nullable=True))
    
    op.create_foreign_key(None, 'documents', 'document_templates', ['template_id'], ['id'])


def downgrade():
    # Remove foreign keys and columns from documents
    op.drop_constraint(None, 'documents', type_='foreignkey')
    op.drop_column('documents', 'generation_settings')
    op.drop_column('documents', 'branding_config')
    op.drop_column('documents', 'template_id')

    # Remove foreign keys and columns from projects
    op.drop_constraint(None, 'projects', type_='foreignkey')
    op.drop_column('projects', 'project_settings')
    op.drop_column('projects', 'custom_fields')
    op.drop_column('projects', 'priority')
    op.drop_column('projects', 'budget')
    op.drop_column('projects', 'end_date')
    op.drop_column('projects', 'start_date')
    op.drop_column('projects', 'po_number')
    op.drop_column('projects', 'contract_number')
    op.drop_column('projects', 'project_manager')
    op.drop_column('projects', 'project_code')
    op.drop_column('projects', 'customer_contact_phone')
    op.drop_column('projects', 'customer_contact_email')
    op.drop_column('projects', 'customer_contact_name')
    op.drop_column('projects', 'customer_organization')
    op.drop_column('projects', 'customer_name')
    op.drop_column('projects', 'organization_id')

    # Remove foreign keys and columns from users
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'timezone')
    op.drop_column('users', 'role')
    op.drop_column('users', 'default_template_id')
    op.drop_column('users', 'organization_id')

    # Drop tables
    op.drop_table('document_templates')
    op.drop_table('organizations')