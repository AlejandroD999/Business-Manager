"""merge alembic heads

Revision ID: ad8e159e2bc4
Revises: 4705d488bcc5, d430cbf5d771
Create Date: 2026-08-07 15:30:53.475476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad8e159e2bc4'
down_revision: Union[str, Sequence[str], None] = ('4705d488bcc5', 'd430cbf5d771')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
