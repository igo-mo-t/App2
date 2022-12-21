from . import app
from .functions import *
from .decorators import *
from flask import request


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/public_room/')
def public_room():
    return selection_1()
    


@app.route('/api/public_rack/')
def public_rack():
    return selection_2()

    
    
@app.route('/api/public_customer/')
def public_customer():
    return selection_3()


@app.route('/api/occupied_rack_customer_room/')
def occupied_rack_customer_room():
    return selection_4()
    
 
@app.route('/api/room_occupied_customer_array/')
def room_occupied_customer_array():
    return selection_5()
    
    
@app.route('/api/room_maximum_rack/')
def room_maximum_rack():
    return selection_6()


@app.route('/api/sum/')
def sum():
    request_args=get_request_args()
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_sum(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])


@app.route('/api/difference/')
def difference():
    request_args=get_request_args()
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_difference(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])


@app.route('/api/product/')
def product():
    request_args=get_request_args()
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_product(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])


@app.route('/api/quotient/')
def quotient():
    request_args=get_request_args()
    @podmen_arg_decor_k(request_args['k'])
    @info_decor
    def f(*args,reverse):
        return f_quotient(*args,reverse=reverse)
    return f(*request_args['args'],reverse=request_args['reverse'])