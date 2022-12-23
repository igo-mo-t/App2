
def info_decor(f):
    """
    
    """
    def f_new(*args,**kwargs):
       print('Function',f.__name__ ,'was called.')
       return f(*args,**kwargs)
    return f_new


def podmen_arg_decor_k(k:int|float):
    """
    
    """
    def podmen_arg_decor(f_new):
        def f_new2(*args,**kwargs):
            args=list(args)
            args[-1]=args[-1]*k
            return f_new(*args,**kwargs)
        return f_new2
    return podmen_arg_decor