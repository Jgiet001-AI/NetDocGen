"""merge_heads

Revision ID: de1689ae5d8c
Revises: 8224de2d6afd, add_ai_analysis_field
Create Date: 2025-07-24 18:29:17.385827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de1689ae5d8c'
down_revision: Union[str, Sequence[str], None] = ('8224de2d6afd', 'add_ai_analysis_field')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
