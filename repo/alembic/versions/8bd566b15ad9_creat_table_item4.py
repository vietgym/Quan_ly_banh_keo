"""creat_table_item4

Revision ID: 8bd566b15ad9
Revises: d6d78cb4e868
Create Date: 2023-12-14 21:49:55.134967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bd566b15ad9'
down_revision: Union[str, None] = 'd6d78cb4e868'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('items',
                    sa.Column('id_item', sa.String, primary_key=True, index=True),
                    sa.Column('id', sa.String),
                    sa.Column('name_lg', sa.String),
                    sa.Column('name_item', sa.String),
                    sa.Column('des_item', sa.String),
                    sa.Column('manufacturers', sa.String),
                    sa.Column('distributor', sa.String),
                    sa.Column('ing_item', sa.String),
                    sa.Column('height', sa.String),
                    sa.Column('cost', sa.String)
                    )


def downgrade() -> None:
    op.drop_table('items')