"""Eliminacion el supervisor de la tabal de books ya que esto fue una prueba y en planes futuros esto no aplica para la escabilidad

Revision ID: 8ae3a1ce6c30
Revises: 7b8292bf17e4
Create Date: 2024-12-19 16:24:49.640884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ae3a1ce6c30'
down_revision: Union[str, None] = '7b8292bf17e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('books', 'supervisor')


def downgrade() -> None:
    op.add_column('books', sa.Column('supervisor', sa.String(length=10), nullable=True))

