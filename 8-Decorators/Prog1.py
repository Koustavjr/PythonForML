import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"The function runs for{end-start}")
        return result
    return wrapper

@timer
def func(n):
    time.sleep(n)

func(4)