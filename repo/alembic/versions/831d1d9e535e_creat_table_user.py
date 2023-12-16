"""creat_table_user

Revision ID: 831d1d9e535e
Revises: 
Create Date: 2023-12-14 20:22:07.509056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '831d1d9e535e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.String, primary_key=True, index=True),
                    sa.Column('name_lg', sa.String),
                    sa.Column('password', sa.String),
                    sa.Column('name', sa.String),
                    sa.Column('email', sa.String),
                    )


def downgrade() -> None:
    op.drop_table('users')
