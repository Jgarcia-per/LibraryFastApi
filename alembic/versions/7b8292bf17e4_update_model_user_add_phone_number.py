"""Update model user add phone number

Revision ID: 7b8292bf17e4
Revises: 4b97b56966f8
Create Date: 2024-12-19 10:53:48.521385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b8292bf17e4'
down_revision: Union[str, None] = '4b97b56966f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(length=15), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
