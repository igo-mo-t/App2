"""Supertest2

Revision ID: 20224f0b4768
Revises: 852da00bc713
Create Date: 2022-12-15 18:24:36.190479

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData


# revision identifiers, used by Alembic.
revision = '20224f0b4768'
down_revision = ''
branch_labels = None
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    meta.reflect(only=('public_customer', 'public_room'))
    public_customer = Table('public_customer', meta)
    public_room = Table('public_room', meta)
    
    op.bulk_insert(
        public_customer,
        [
            {'id':6, 'name':'Клиент-6'},
            {'id':7, 'name':'Клиент-7'}
        ])

    op.bulk_insert(
        public_room,
        [
            {'id':5, 'name':'Room 5'}
        ]
    )

def downgrade():
    pass
