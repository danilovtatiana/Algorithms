#bubble sort

list = [2,7,1,9,3]

n = len(list)

for i in range(n):
    for j in range(0,n-i-1):
        if list[j] > list[j+1]:
            #list[j],list[j+1] = list[j+1],list[j]
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
print(list)

