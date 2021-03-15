#create a function that calculate the sum of number's digits

def sum(n):
    s = 0
    while n!=0:
        ld = int(n % 10)
        n = int(n / 10)
        s += ld
    return s
print(sum(123))

#create a function that find the max digit from a number

def maximum(n):
    max = 0
    while n!=0:
        ld = int(n % 10)
        if ld > max:
            max = ld
        n = int(n / 10)
    return max

print(maximum(12534))

#power of a number

def power(n):
    return n*n
print(power(6))

#recursion function factorial

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(7))