def debug(func):
    def wrapper(*args,**kwargs):
        arg_list=",".join(str(arg) for arg in args)
        kwarg_list=",".join(f"{k}={v}" for k,v in kwargs.items())
        
        print(f"{func.__name__} has {arg_list} args and {kwarg_list} kwargs")
        result=func(*args,**kwargs)
        return result
    return wrapper

@debug
def func(name,greeting="Hello"):
    print(f"{greeting}, {name}")
    


func("chai",greeting="Hanji")
    
func(name="World")