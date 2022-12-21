from . import db
from .models import Room, Rack, Customer
from flask import request
import json



def selection_1():
    query = db.session.query(Room.id,Room.name).all()
    return {'Room':[{'id':id,'name':name} for id,name in query]}


def selection_2():
    query = db.session.query(Rack.id,Rack.name,Rack.size,Rack.state,Rack.customer_id,Rack.room_id).all()
    return {'Rack':[{'id':id,'name':name,'size':size,'state':state,'customer_id':customer_id,'room_id':room_id} 
                    for id,name,size,state,customer_id,room_id in query]}
    
    
def selection_3():
    query = db.session.query(Customer.id,Customer.name).all()
    return {'Customer':[{'id':id,'name':name} for id,name in query]}


def selection_4():
    query = db.session.query(Rack.id,Rack.name,Customer.name,Room.name)
    query = query.join(Room).join(Customer).filter(Rack.state=='occupied').all()
    return [{'id_rack':rack_id,'rack_name':rack_name,'customer_name':customer_name,'room_name':room_name}
            for rack_id,rack_name,customer_name,room_name in query]
    
    
def selection_5():
    query = db.session.query(Room.id,Room.name,db.func.array_agg(Rack.customer_id))
    query = query.outerjoin(Room.racks).filter(Rack.state=='occupied').group_by(Room.id,Room.name).all()
    return [{'id':id,'name':name,'array_customers':array_customers} for id,name,array_customers in query]        


def selection_6():
    subq = db.session.query(Room.id,db.func.max(Rack.size).label('max_size'))
    subq = subq.outerjoin(Room.racks).group_by(Room.id).subquery()
    query = db.session.query(subq.c.id,db.func.min(Rack.id),subq.c.max_size)
    query = query.outerjoin(Rack, subq.c.id==Rack.room_id)
    query = query.group_by(subq.c.id, subq.c.max_size).all()
    return [{'room_id':room_id,'rack_id':rack_id,'rack_size':rack_size} for room_id,rack_id,rack_size in query]        


def get_request_args():
    args = request.args.get('args','0')
    args = [json.loads(arg) for arg in args.split(',')]
    k = request.args.get('k',1)
    k = json.loads(k)
    reverse = request.args.get('reverse')
    if reverse:
        reverse = json.loads(reverse.lower())              # исключение, ошибка если другая строка
    return {'args':args,'k':k,'reverse':reverse} 


def f_sum(*args,reverse=False):
    a=0
    if reverse:
        args = args[::-1]
    for i in args:
        a+=i
    return {'Arguments':args,'Reverse':reverse,'Sum result':a}
    

def f_difference(*args,reverse=False):
    if reverse:
        args = args[::-1]
    a=args[0]
    for i in args[1:]:
        a-=i
    return {'Arguments':args,'Reverse':reverse,'Difference result':a}  


def f_product(*args,reverse=False):
    if reverse:
        args = args[::-1]
    a=args[0]
    for i in args[1:]:
        a*=i
    return {'Arguments':args,'Reverse':reverse,'Product result':a}
    

def f_quotient(*args,reverse=False):
    if reverse:
        args = args[::-1]
    a=args[0]
    for i in args[1:]:
        a/=i
    return {'Arguments':args,'Reverse':reverse,'Quotient result':a}
 
     