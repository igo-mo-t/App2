from . import db


class Room(db.Model):
    __tablename__ = 'public_room'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50))
    racks = db.relationship('Rack', backref = 'room')
    
    
class Rack(db.Model):
    __tablename__ = 'public_rack'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50))
    size = db.Column(db.Integer())
    state = db.Column(db.String(50))
    customer_id = db.Column(db.Integer(), db.ForeignKey('public_customer.id'))
    room_id = db.Column(db.Integer(), db.ForeignKey('public_room.id'))

    
class Customer(db.Model):
    __tablename__ = 'public_customer'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50))
    racks = db.relationship('Rack', backref = 'customer')