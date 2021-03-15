#check if the point is inside the circle

import math

x = float(input())
y = float(input())
r = float(input())

h = math.sqrt((x*x)+(y*y))

if h <= r:
    print("The point is inside the circle")
else:
    print("The point is outside the circle")
