from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://test:test@127.0.0.1:5433/test'

db=SQLAlchemy(app)
migrate=Migrate(app, db)

@app.before_first_request
def create_table():
    db.create_all()
    
class Room(db.Model):
    __tablename__ = 'public_room'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50))
    racks = db.relationship('Rack', backref = 'room')
    
    @property
    def room_occupied_customers(self):
        return {
            'Room_id': self.id,
            'Room_name': self.name,
            'Customer_id': [rack.occupied_customers for rack in self.racks if rack.occupied_customers]
        }
    
 
class Rack(db.Model):
    __tablename__ = 'public_rack'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50))
    size = db.Column(db.Integer())
    state = db.Column(db.String(50))
    customer_id = db.Column(db.Integer(), db.ForeignKey('public_customer.id'))
    room_id = db.Column(db.Integer(), db.ForeignKey('public_room.id'))

    @property
    def occupied_customers(self):
        if self.state == 'occupied':
            return self.customer_id
    

class Customer(db.Model):
    __tablename__ = 'public_customer'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50))
    racks = db.relationship('Rack', backref = 'customer')
    
  

    # def __repr__(self):
    #     return f'{self.id}, {self.name}'

# 1)
# public_room = Room.query.all()
# public_rack = Rack.query.all()
# public_customer = Customer.query.all()

# 2) 
# db.session.query(Rack.id,Rack.name,Customer.name,Room.name).join(Room).join(Customer).filter(Rack.state=='occupied').all()

# 3)
# rooms = =db.session.query(Room).all()
# rooms_occupied_customers=[room.room_occupied_customers for room in rooms]
# Вариант 2
# db.session.query(Room.id,Room.name,db.func.array_agg(Rack.customer_id)).outerjoin(Room.racks).filter(Rack.state=='occupied').group_by(Room.id,Room.name).all()

# 4) subq=db.session.query(Rack.room_id,db.func.max(Rack.size).label('max_size')).group_by(Rack.room_id).subquery()
# db.session.query(subq.c.room_id,db.func.min(Rack.id),subq.c.max_size).join(subq, Rack.room_id==subq.c.room_id).filter(Rack.size==subq.c.max_size).group_by(subq.c.room_id, subq.c.max_size).all()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)