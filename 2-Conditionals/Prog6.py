distance= int(input("Enter distance "))

if distance<3:
    action="Walk"
elif distance<15:
    action="Bike"
else:
    action="Car"

print(action)
