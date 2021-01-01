import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
create foo table

Revision ID: d2bc451d4432
Revises: bb14e8a780ce
Create Date: 2020-12-30 11:34:59.203108
"""

# Revision identifiers, used by Alembic.
revision = 'd2bc451d4432'
down_revision = 'bb14e8a780ce'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('foos', sa.Column('hello_on', AwareDateTime(),default=tzware_datetime))



def downgrade():
    op.drop_column('foos', 'hello_on')
