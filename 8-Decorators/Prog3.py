import time
def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        print(*args)
        print(args)
        if args in cache_value:
            return cache_value[args]
        result =func(*args)
        cache_value[args]=result
        
        return result
    return wrapper


@cache
def func(a,b):
    time.sleep(2)
    return a+b

func(2,3)
func(2,3)
func(4,5)