from project import app
from project.functions import selection_1, selection_2
from flask import json

def test_sum():
    """
    GIVEN a Flask application
    WHEN the '/api/sum/' page is requested (GET)
    THEN correct response
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/sum/?args=16,2,4&k=2&reverse=True')
        assert b'{"Arguments":[8,2,16],"Reverse":true,"Sum result":26}' in response.data
        response = test_client.get('/api/sum/?args=&k=2&reverse=True')
        assert b'args must be numbers of type: int,float. Also reverse must be: bool,int or float.' in response.data
        response = test_client.get('/api/sum/?&k=2&reverse=True')
        assert b'You need to enter args in the request arguments.' in response.data


def test_difference():
    """
    GIVEN a Flask application
    WHEN the '/api/difference/' page is requested (GET)
    THEN correct response
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/difference/?args=16,2,4&k=2&reverse=True')
        assert b'{"Arguments":[8,2,16],"Difference result":-10,"Reverse":true}' in response.data
        response = test_client.get('/api/difference/?args=&k=2&reverse=True')
        assert b'args must be numbers of type: int,float. Also reverse must be: bool,int or float.' in response.data
        response = test_client.get('/api/difference/?&k=2&reverse=True')
        assert b'You need to enter args in the request arguments.' in response.data


def test_product():
    """
    GIVEN a Flask application
    WHEN the '/api/product/' page is requested (GET)
    THEN correct response
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/product/?args=16,2,4&k=2&reverse=True')
        assert b'{"Arguments":[8,2,16],"Product result":256,"Reverse":true}' in response.data
        response = test_client.get('/api/product/?args=&k=2&reverse=True')
        assert b'args must be numbers of type: int,float. Also reverse must be: bool,int or float.' in response.data
        response = test_client.get('/api/product/?&k=2&reverse=True')
        assert b'You need to enter args in the request arguments.' in response.data


def test_quotient():
    """
    GIVEN a Flask application
    WHEN the '/api/quotient/' page is requested (GET)
    THEN correct response
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/quotient/?args=16,2,4&k=2&reverse=True')
        assert b'{"Arguments":[8,2,16],"Quotient result":0.25,"Reverse":true}' in response.data
        response = test_client.get('/api/quotient/?args=&k=2&reverse=True')
        assert b'args must be numbers of type: int,float. Also reverse must be: bool,int or float.' in response.data
        response = test_client.get('/api/quotient/?&k=2&reverse=True')
        assert b'You need to enter args in the request arguments.' in response.data                
        
        
        
def test_rack():
    """
    GIVEN a Flask application
    WHEN the '/api/public_rack/' page is requested (GET)
    THEN correct response
    """
    import sys
    with app.test_client() as test_client:
        response = test_client.get('/api/public_rack/')
        data = json.loads(response.get_data(as_text=True))
        assert selection_2()==data
      
        
        
def test_room():
    """
    GIVEN a Flask application
    WHEN the '/api/quotient/' page is requested (GET)
    THEN correct response
    """

    import sys
    with app.test_client() as test_client:
        response = test_client.get('/api/public_room/')
        data = json.loads(response.get_data(as_text=True))
        assert selection_1()==data
      
        
        