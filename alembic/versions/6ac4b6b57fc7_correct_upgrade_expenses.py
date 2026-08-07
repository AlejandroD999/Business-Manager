"""correct_upgrade_expenses

Revision ID: 6ac4b6b57fc7
Revises: fb3ef996fac3
Create Date: 2026-08-07 15:52:25.261241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ac4b6b57fc7'
down_revision: Union[str, Sequence[str], None] = 'fb3ef996fac3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
            "expenses",
            "date",
            type_=sa.Date
            )

def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
            "expenses",
            "date",
            type_=sa.Datetime()
            )
