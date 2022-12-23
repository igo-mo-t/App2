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
    meta.reflect(only=('public_customer', 'public_room', 'public_rack'))
    public_customer = Table('public_customer', meta)
    public_room = Table('public_room', meta)
    public_rack = Table('public_rack', meta)
    
    op.bulk_insert(
        public_customer,
        [
            {'id':1, 'name':'Клиент-1'},
            {'id':2, 'name':'Клиент-2'},
            {'id':3, 'name':'Клиент-3'}
        ])

    op.bulk_insert(
        public_room,
        [
            {'id':1, 'name':'Room1'},
            {'id':2, 'name':'Room2'},
            {'id':3, 'name':'Room3'},
            {'id':4, 'name':'Room4'}
        ])

    op.bulk_insert(
        public_rack,
        [
            {'id':1, 'name':'Rack1', 'size':42, 'state':'occupied', 'customer_id':1, 'room_id':1},
            {'id':2, 'name':'Rack2', 'size':42, 'state':'occupied', 'customer_id':2, 'room_id':1},
            {'id':3, 'name':'Rack3', 'size':21, 'state':'free', 'customer_id':3, 'room_id':1},
            {'id':4, 'name':'Rack4', 'size':42, 'state':'occupied', 'customer_id':1, 'room_id':2},
            {'id':5, 'name':'Rack5', 'size':42, 'state':'free', 'customer_id':1, 'room_id':2},
            {'id':6, 'name':'Rack6', 'size':47, 'state':'free', 'customer_id':2, 'room_id':3},
            {'id':7, 'name':'Rack7', 'size':42, 'state':'occupied', 'customer_id':1, 'room_id':3},
            {'id':8, 'name':'Rack8', 'size':21, 'state':'occupied', 'customer_id':1, 'room_id':3}
        ])

def downgrade():
    pass
    # meta = MetaData(bind=op.get_bind())
    # meta.reflect(only=('public_customer', 'public_room', 'public_rack'))
    # public_customer = Table('public_customer', meta)
    # public_room = Table('public_room', meta)
    # public_rack = Table('public_rack', meta)
    
    # op.bulk_insert(
    #     public_customer,
    #     [
    #         {'id':null, 'name':null},
    #         {'id':null, 'name':null},
    #         {'id':null, 'name':null}
    #     ])

    # op.bulk_insert(
    #     public_room,
    #     [
    #         {'id':, 'name':},
    #         {'id':, 'name':},
    #         {'id':, 'name':},
    #         {'id':, 'name':}
    #     ])

    # op.bulk_insert(
    #     public_rack,
    #     [
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':},
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':},
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':},
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':},
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':},
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':},
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':},
    #         {'id':, 'name':, 'size':, 'state':, 'customer_id':, 'room_id':}
    #     ])

