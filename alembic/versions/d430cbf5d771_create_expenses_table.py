"""create_expenses_table

Revision ID: d430cbf5d771
Revises: 6b3470c4db71
Create Date: 2026-07-23 08:58:14.920035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd430cbf5d771'
down_revision: Union[str, Sequence[str], None] = None 
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
            'expenses',
            sa.Column("id", sa.BIGINT, primary_key=True),
            sa.Column("user_id", sa.BIGINT, nullable=False),
            sa.Column("description", sa.String(255)), 
            sa.Column("amount", sa.FLOAT, nullable=False),
            sa.Column("date", sa.String(255), nullable=False),
            # TODO Implement payment_method and category table foreign keys

            )


def downgrade() -> None:
    op.drop_table("expenses")
