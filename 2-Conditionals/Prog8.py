password=input("Enter Password ")

length=len(password)

if length<6:
    criteria="Weak"
elif length<=10:
    criteria="Medium"
else:
    criteria="Strong"

print(criteria)
