'''
Count the number of even elements in an array of zero-terminated integers. Zero itself does not need to be taken into account
'''

list = [2,3,4,2,5,6,0]
even_numbers = 0

for i in list:
    if i % 2 == 0 and i !=0:
        even_numbers += 1
print(even_numbers)