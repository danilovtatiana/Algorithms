# calculate the sum of all digits fro the number

n = 123
sum = 0

while n != 0:
    last_digit = n % 10
    n = int(n / 10)
    sum += last_digit
print(sum)


#calculate the sum of all digits from the random number

from random import randint

n = randint(100,999)
print("n = ",n)

sum = 0

while n != 0:
    last_digit = n % 10
    n = int(n / 10)
    sum += last_digit
print(sum)

