
import sys


def info_decor(f):
    """
    Takes a function and adds console output 
    to it when it is called
    """
    def f_new(*args,**kwargs):
       print('Function',f.__name__ ,'was called.', file=sys.stderr)
       return f(*args,**kwargs)
    return f_new


def podmen_arg_decor_k(k:int|float):
    """
    Takes a function and multiplies 
    its last argument by "k"
    """
    def podmen_arg_decor(f_new):
        def f_new2(*args,**kwargs):
            args=list(args)
            args[-1]=args[-1]*k
            return f_new(*args,**kwargs)
        return f_new2
    return podmen_arg_decor