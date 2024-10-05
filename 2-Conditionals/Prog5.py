weather= input("weather ")
weather.capitalize()


if weather=='Sunny':
    action="Go for a walk"
elif weather=='Rainy':
    action='Read a book'
else:
    action="Build a snowman"

print(action)    