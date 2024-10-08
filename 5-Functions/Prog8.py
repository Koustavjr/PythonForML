def sum_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        print("Keys: ",key)
        print("values:",value)
    
sum_all(a=1,b=3)