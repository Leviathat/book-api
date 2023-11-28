"""book table

Revision ID: 6ede531510b8
Revises: 
Create Date: 2023-11-28 14:49:44.592063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String

# revision identifiers, used by Alembic.
revision: str = '6ede531510b8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books',
        Column('id', Integer, primary_key=True, index=True),
        Column('title', String, index=True),
        Column('description', String, index=True)
    )


def downgrade() -> None:
    pass
