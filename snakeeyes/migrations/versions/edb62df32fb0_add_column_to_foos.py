import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
add column to foos

Revision ID: edb62df32fb0
Revises: d2bc451d4432
Create Date: 2020-12-30 11:37:02.083493
"""

# Revision identifiers, used by Alembic.
revision = 'edb62df32fb0'
down_revision = 'd2bc451d4432'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
