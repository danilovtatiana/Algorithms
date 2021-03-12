'''
Find Cartesian coordinates of the point and write in what part this point is
'''

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("First Part")
elif x < 0 and y > 0:
    print("Second Part")
elif x < 0 and y < 0:
    print("Third Part")
else:
    print("Fourth Part")
