'''
The deposit in the bank is x euro. It increases annually by p percent. Each year, the amount of the deposit becomes larger. It is necessary to determine in how many years the contribution will be at least y euro.
'''

x = int(input())
p = int(input())
y = int(input())

i = 0
p2 = int((p*x)/100)
print(p2)

while x < y:
    x = x + p2
    i += 1
print(i)