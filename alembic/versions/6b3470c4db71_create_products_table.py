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
    op.create_table(
        'products',
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("user_id", sa.BIGINT, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
        sa.Column("description", sa.String(255)),
        sa.UniqueConstraint("user_id", "name")
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("products")
