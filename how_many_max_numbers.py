'''
count how many max numbers are in an array and in a number
'''

n1 = [2,4,4,4,2]

max1 = 0
count1 = 0

for i in n1:
    if i > max1:
        max1 = i
        count1 = 1
    elif i == max1:
        count1 +=1
print(count1)

n2 = 66436662

max2 = 0
count2 = 0

while n2!=0:
    ld = int(n2 % 10)
    n2 = int(n2 / 10)
    if ld > max2:
        max2 = ld
        count2 = 1
    elif ld == max2:
        count2 += 1
print(count2)

