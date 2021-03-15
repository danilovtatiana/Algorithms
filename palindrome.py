#check if number or string is a palindrome

def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
palindrome("abc")

num = int(input())
temp = num
rev = 0

while num!=0:
    ld = int(num % 10)
    rev = rev*10 + ld
    num = int(num / 10)

if temp == rev:
    print("Palindrome")
else:
    print("Not palindrome")