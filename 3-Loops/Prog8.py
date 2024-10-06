n=int(input("Enter number "))
flag=True
if n>1:
    for i in range (2,n):
        if(n%i)==0:
            flag=False
            break

if flag==True:
    print("Prime")
else:
    print("Not Prime")