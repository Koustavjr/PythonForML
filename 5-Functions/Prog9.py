def even(num):
    for i in range(2,num+1,2):
        #return i
        yield i
    

print(even(5))

"""
    Error 
for i in even(5):
    print(i)
"""

for i in even(11):
    print(i)
