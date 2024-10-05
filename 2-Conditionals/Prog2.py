age=int(input("Enter age "))
day= input("Enter day ")

day.lower()

price=12 if age>18 else 8

if day=="wednesday":
    price-=2

print(price)