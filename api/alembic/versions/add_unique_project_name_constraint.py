"""Add unique constraint for project names per user

Revision ID: add_unique_project_name
Revises: 
Create Date: 2025-07-24

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_unique_project_name'
down_revision = 'de1689ae5d8c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create a unique index on lowercase project name and owner_id
    # This ensures no two projects can have the same name (case-insensitive) for the same user
    op.create_index(
        'ix_projects_name_owner_unique',
        'projects',
        [sa.text('LOWER(name)'), 'owner_id'],
        unique=True,
        postgresql_where=sa.text("status != 'DELETED'")
    )


def downgrade() -> None:
    # Drop the unique index
    op.drop_index('ix_projects_name_owner_unique', table_name='projects')