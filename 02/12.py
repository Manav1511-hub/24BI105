# 24BIT105

# Que-12

import math

x = int(input("Enter x coordinate : "))
y = int(input("Enter y coordinate : "))
r = int(input("Enter radius : "))

d = math.sqrt(pow(x,2) + pow(y,2))

if d == r:
    print("The point lies on the circle.")
elif d < r:
    print("The point lies inside the circle.")
else:
    print("The point lies outside the circle.")
