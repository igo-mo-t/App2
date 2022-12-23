from . import app
from .functions import *
from .decorators import *
from flask import request
from typing import Any


@app.route('/')
def hello_world() -> str:
    """
    Returns a 'Hello World!' response to the client.
    """
    return 'Hello World!'



@app.route('/api/public_room/')
def public_room() -> dict[str, list[dict[str, Any]]]:
    """
    Returns the response to the client 
    as the result of the "selection_1" function
    """
    return selection_1()
    


@app.route('/api/public_rack/')
def public_rack() -> dict[str, list[dict[str, Any]]]:
    """
    Returns the response to the client 
    as the result of the "selection_2" function
    """
    return selection_2()

    
    
@app.route('/api/public_customer/')
def public_customer() -> dict[str, list[dict[str, Any]]]:
    """
    Returns the response to the client 
    as the result of the "selection_3" function
    """
    return selection_3()



@app.route('/api/occupied_rack_customer_room/')
def occupied_rack_customer_room() -> list[dict[str, Any]]:
    """
    Returns the response to the client 
    as the result of the "selection_4" function
    """
    return selection_4()
    
 
 
@app.route('/api/room_occupied_customer_array/')
def room_occupied_customer_array() -> list[dict[str, Any]]:
    """
    Returns the response to the client 
    as the result of the "selection_5" function
    """
    return selection_5()
    
    
    
@app.route('/api/room_maximum_rack/')
def room_maximum_rack() -> list[dict[str, Any]]:
    """
    Returns the response to the client 
    as the result of the "selection_6" function
    """
    return selection_6()



@app.route('/api/sum/')
def sum() -> str | dict[str, Any]:
    """
    Returns information if the request arguments were passed incorrectly.
    
    Returns a response to the client as the result 
    of a decorated "f_sum" function that takes the request arguments.
    
    Decorators: argument substitution and information in the console.
    """
    request_args=get_request_args()
    if type(request_args) is not dict:
        return request_args
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_sum(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])



@app.route('/api/difference/')
def difference() -> str | dict[str, Any]:
    """
    Returns information if the request arguments were passed incorrectly.
    
    Returns a response to the client as the result 
    of a decorated "f_difference" function that takes the request arguments.

    Decorators: argument substitution and information in the console.
    """
    request_args=get_request_args()
    if type(request_args) is not dict:
        return request_args
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_difference(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])



@app.route('/api/product/')
def product() -> str | dict[str, Any]:
    """
    Returns information if the request arguments were passed incorrectly.
    
    Returns a response to the client as the result 
    of a decorated "f_product" function that takes the request arguments.

    Decorators: argument substitution and information in the console.
    """
    request_args=get_request_args()
    if type(request_args) is not dict:
        return request_args
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_product(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])



@app.route('/api/quotient/')
def quotient() -> str | dict[str, Any]:
    """
    Returns information if the request arguments were passed incorrectly.
    
    Returns a response to the client as the result 
    of a decorated "f_quotient" function that takes the request arguments.

    Decorators: argument substitution and information in the console.
    """
    request_args=get_request_args()
    if type(request_args) is not dict:
        return request_args
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_quotient(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])