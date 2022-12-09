from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

db=SQLAlchemy(app)


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
    customer = db.Column(db.Integer(), db.ForeignKey('public_customer.id'))
    room_id = db.Column(db.Integer(), db.ForeignKey('public_room.id'))


class Customer(db.Model):
    __tablename__ = 'public_customer'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50))
    racks = db.relationship('Rack', backref = 'customer')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)