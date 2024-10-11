# username="abc"

# def test():
#     username="chai"
#     print(username)

# #print(username)    
# test()

# x=99
# def func(y):
#     z=x+y
#     return z


# result=func(1)
# print(result) 

# def func2():
#     global x
#     x=12
    
    
# func2()
# print(x)

x=99

def f1():
    x=88
    def f2():
        print(x)
    f2()
f1()


x=99

def f1():
    x=88
    def f2():
        print(x)
    return f2
result= f1()

result()

def coder(num):
    def actual(x):
        return x**num
    return actual

f=coder(2) # it has reference to both actual() method 
            # as well as reference to the num variable of method coder()
g=coder(3)

print(f)
print(f(3))