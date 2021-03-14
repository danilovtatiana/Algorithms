n = int(input())

if n <=2:
    if n == 2:
        print("Number is prime")
    else:
        print("Number must be bigger")

if n > 2:
    is_prime = True
    for i in range(3,n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print("Number is prime")
    else:
        print("Number is not prime")