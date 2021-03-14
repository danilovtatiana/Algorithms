n = [2,8,35,88,12,99]

max = 0

for i in n:
    if i > max and i % 2 ==0:
        max = i
print(max)

x = 983887

max_num = 0

while x!=0:
    ld = int(x%10)
    x = int(x/10)
    if ld > max_num and ld % 2 == 0:
        max_num = ld
print(max_num)