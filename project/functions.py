from . import db
from .models import Room, Rack, Customer
from flask import request
import json
from typing import Any



def selection_1() -> dict[str, list[dict[str, Any]]]:
    """
    Makes a query to the database 
    and returns a dictionary with a list of room dictionaries.
    """
    query = db.session.query(Room.id,Room.name).all()
    return {'Room':[{'id':id,'name':name} for id,name in query]}



def selection_2() -> dict[str,list[dict[str, Any]]]:
    """
    Makes a query to the database 
    and returns a dictionary with a list of rack dictionaries.
    """
    query = db.session.query(Rack.id,Rack.name,Rack.size,Rack.state,Rack.customer_id,Rack.room_id).all()
    return {'Rack':[{'id':id,'name':name,'size':size,'state':state,'customer_id':customer_id,'room_id':room_id} 
                    for id,name,size,state,customer_id,room_id in query]}
    
    
    
def selection_3() -> dict[str,list[dict[str, Any]]]:
    """
    Makes a query to the database 
    and returns a dictionary with a list of customer dictionaries.
    """
    query = db.session.query(Customer.id,Customer.name).all()
    return {'Customer':[{'id':id,'name':name} for id,name in query]}



def selection_4() -> list[dict[str, Any]]:
    """
    Makes a query to the database
    and returns a list of occupied rack dictionaries 
    with the name of the room 
    each rack is in and the name of the customer it belongs to.
    """
    query = db.session.query(Rack.id,Rack.name,Customer.name,Room.name)
    query = query.join(Room).join(Customer).filter(Rack.state=='occupied').all()
    return [{'id_rack':rack_id,'rack_name':rack_name,'customer_name':customer_name,'room_name':room_name}
            for rack_id,rack_name,customer_name,room_name in query]
    
    
    
def selection_5() -> list[dict[str, Any]]:
    """
    Makes a query to the database
    and returns a list of dictionaries of all rooms 
    with an array of room IDs attached
    to each customers who have occupied counters in this room.
    """
    query = db.session.query(Room.id,Room.name,db.func.array_agg(Rack.customer_id))
    query = query.outerjoin(Room.racks).filter(Rack.state=='occupied').group_by(Room.id,Room.name).all()
    return [{'id':id,'name':name,'array_customers':array_customers} for id,name,array_customers in query]        



def selection_6() -> list[dict[str, Any]]:
    """
    Makes a query to the database
    and returns a list of dictionaries of all rooms 
    with the maximum size racks in each room.
    """
    subq = db.session.query(Room.id,db.func.max(Rack.size).label('max_size'))
    subq = subq.outerjoin(Room.racks).group_by(Room.id).subquery()
    query = db.session.query(subq.c.id,db.func.min(Rack.id),subq.c.max_size)
    query = query.outerjoin(Rack, subq.c.id==Rack.room_id)
    query = query.group_by(subq.c.id, subq.c.max_size).all()
    return [{'room_id':room_id,'rack_id':rack_id,'rack_size':rack_size} for room_id,rack_id,rack_size in query]        



def get_request_args() -> dict[str, Any]:
    """
    Defines the request arguments 
    and returns them in a dictionary.
    
    Returns informational messages 
    if arguments are passed incorrectly.
    """
    try:
        args = request.args.get('args')
        args = [json.loads(arg) for arg in args.split(',')]
        k = request.args.get('k','1')
        k = json.loads(k)
        reverse = request.args.get('reverse')
        if reverse:
            reverse = json.loads(reverse.lower())             
        return {'args':args,'k':k,'reverse':reverse}
    
    except AttributeError:
        return 'You need to enter args in the request arguments.'
    
    except:
        return 'args must be numbers of type: int,float. Also reverse must be: bool,int or float.'
         


def f_sum(*args,reverse: bool | int | None = False) -> dict[str, Any]:
    """
    It takes arguments and returns the result of their sum.
    Depending on the value of "reverse" changes the order of calculations.
    """
    a=0
    if reverse:
        args = args[::-1]
    for i in args:
        a+=i
    return {'Arguments':args,'Reverse':reverse,'Sum result':a}
    


def f_difference(*args,reverse: bool | int | None = False) -> dict[str, Any]:
    """
    It takes arguments and returns the result of their difference.
    Depending on the value of "reverse" changes the order of calculations.
    """
    if reverse:
        args = args[::-1]
    a=args[0]
    for i in args[1:]:
        a-=i
    return {'Arguments':args,'Reverse':reverse,'Difference result':a}  



def f_product(*args,reverse: bool | int | None = False) -> dict[str, Any]:
    """
    It takes arguments and returns the result of their product.
    Depending on the value of "reverse" changes the order of calculations.
    """
    if reverse:
        args = args[::-1]
    a=args[0]
    for i in args[1:]:
        a*=i
    return {'Arguments':args,'Reverse':reverse,'Product result':a}
    


def f_quotient(*args,reverse: bool | int | None = False) -> dict[str, Any]:
    """
    It takes arguments and returns the result of their division.
    Depending on the value of "reverse" changes the order of calculations.
    """
    try:
        if reverse:
            args = args[::-1]
        a=args[0]
        for i in args[1:]:
            a/=i
        return {'Arguments':args,'Reverse':reverse,'Quotient result':a}
    
    except ZeroDivisionError as e:
        return f'{e}'
 
 