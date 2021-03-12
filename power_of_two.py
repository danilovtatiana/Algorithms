n = int(input())

if n <= 0 or n >= 20:
    print("Exit")
else:
    for i in range(0,n+1):
        print(i*i)