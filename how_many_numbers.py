'''
Write how many digits are in a number
'''

n = int(input())

count = 0

while n != 0:
    n = int(n / 10)
    count += 1
print(count)