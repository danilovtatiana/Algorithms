#find the greatest common factor

a = int(input())
b = int(input())

while a!=0 and b!=0:
    if a > b:
        a = a % b
        b = b - a
    else:
        b = b % a
        a = a - b
print(a+b)