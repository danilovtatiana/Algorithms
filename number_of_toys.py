# //Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
# //
# //Note Each toy can be purchased only once.
# //
# //Example
# // prices = [1,2,3,4]
# // k = 7
# //
# //The budget is 7 units of currency. He can buy items that cost [1,2,3] for 6, or [3,4] for 7 units. The maximum is 3 items.
# //
# //Sample Input
# //
# //7 50
# //1 12 5 111 200 1000 10
# //Sample Output
# //
# //4

def list_sort(list):
   #bubble sort
    n = len(list)
    temp = 0
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list



def number_of_toys(list,k):
    #sort list
    #if list.sorted is not accepted, the list will be sorted manually
    count = 0
    sum = 0
    for i in list_sort(list):
        if sum + i <= k and i <= k:
            sum += i
            count += 1
    return count

print(number_of_toys([5,2,1,6],7))
