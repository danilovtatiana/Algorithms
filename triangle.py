#what type of triangle is it? acute, right or obtuse
a = int(input())
b = int(input())
c = int(input())

if a+b > c and a+c > b and b+c > a:
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print("right")
    elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")