'''
Count how many zero are in the number
'''

n = int(input())

count = 0

while n != 0:
    n = int(n/10)
    last_digit = n % 10
    if last_digit == 0:
        count +=1
print(count)