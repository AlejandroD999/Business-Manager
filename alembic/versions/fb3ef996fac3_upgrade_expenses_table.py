"""upgrade expenses table

Revision ID: fb3ef996fac3
Revises: ad8e159e2bc4
Create Date: 2026-08-07 15:33:04.835481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb3ef996fac3'
down_revision: Union[str, Sequence[str], None] = 'ad8e159e2bc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.create_table(
            'expenses',
            sa.Column("id", sa.BIGINT, primary_key=True),
            sa.Column("user_id", sa.BIGINT, nullable=False),
            sa.Column("description", sa.String(255)), 
            sa.Column("amount", sa.Float, nullable=False),
            sa.Column("date", sa.DateTime, nullable=False),
            )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('expenses')
