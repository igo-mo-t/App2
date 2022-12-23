from project.functions import *

def test_f_sum():
    """
    GIVEN f_sum function
    WHEN function call
    THEN correct return
    """
    assert f_sum(1,2,3,reverse=True) == {'Arguments':(3,2,1),'Reverse':True,'Sum result':6}
    
    
def test_f_difference():    
    """
    GIVEN f_difference function
    WHEN function call
    THEN correct return
    """
    assert f_difference(1,2,3) == {'Arguments':(1,2,3),'Reverse':False,'Difference result':-4}


def test_f_product():    
    """
    GIVEN f_product function
    WHEN function call
    THEN correct return
    """
    assert f_product(1,2,3,reverse=1) == {'Arguments':(3,2,1),'Reverse':1,'Product result':6}


def test_f_quotient():    
    """
    GIVEN f_quotient function
    WHEN function call
    THEN correct return
    """
    assert f_quotient(1,2,3,reverse=1) == {'Arguments':(3,2,1),'Reverse':1,'Quotient result':1.5}
    assert f_quotient(2,1,0) == 'division by zero' or 'float division by zero'