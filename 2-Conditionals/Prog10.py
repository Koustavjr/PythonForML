pet=input("Enter pet ").lower()
age=int(input("Enter age "))


if pet=='dog':
    if age<2:
        food="Puppy Food"
    else:
        food="Senior Dog food"
elif pet=='cat':
    if age<5:
        food="Baby cat food"
    else:
        food="Senior cat food"
else:
    exit()
    
print(food)