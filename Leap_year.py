'''
Write a program to determine whether a given year is a leap year.

A year is a leap year if the following conditions are satisfied:
The year is multiple of 400.
The year is multiple of 4 and not multiple of 100.
'''

n = int(input())

if n % 100 == 0:
    print("usual year")
elif n % 4 == 0 or n % 400 == 0:
    print("leap year")
else:
    print("usual year")