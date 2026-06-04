"""create_products_table

Revision ID: 6b3470c4db71
Revises: 4705d488bcc5
Create Date: 2026-06-03 20:35:31.189138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b3470c4db71'
down_revision: Union[str, Sequence[str], None] = '4705d488bcc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
