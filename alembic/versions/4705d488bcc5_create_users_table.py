"""Create users table

Revision ID: 4705d488bcc5
Revises: 
Create Date: 2026-04-29 09:57:45.160685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4705d488bcc5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("username", sa.String(255), nullable=False),
        sa.Column("password", sa.String(255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("users")
