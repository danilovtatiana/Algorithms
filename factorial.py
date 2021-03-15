def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(7))

n = 7
factorial = 1

if n < 0:
    print("Does not exist")
elif n == 1:
    factorial = 1
else:
    for i in range(1,n+1):
        factorial = factorial * i
print(factorial)