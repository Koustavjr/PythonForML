import math

def circle(r):
    area=round(math.pi*r**2,2)
    circum=round(2*math.pi*r,2)
    return area,circum

a,c=circle(3)

print('Area ',a ,"Circumference ",c)