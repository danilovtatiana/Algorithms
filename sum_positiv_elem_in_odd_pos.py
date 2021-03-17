'''
calculate the sum of numbers from an array that are non negative and on the odd positions
'''
list = [1,0,5,-7,9,3]
n = len(list)
sum = 0
for i in range(n):
    if i % 2 != 0 and list[i] > 0:
        sum = sum +list[i]
print(sum)

def sum_positiv_elem_in_odd_pos(arr): #function
    n = len(list)
    sum = 0
    for i in range(n):
        if i % 2 != 0 and list[i] > 0:
            sum = sum + list[i]
    return sum
print(sum_positiv_elem_in_odd_pos([1,0,5,-7,9,3]))