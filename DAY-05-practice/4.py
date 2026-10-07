#palindrome number

a = int (input("Enter the Number : "))

copy = a
rev = 0

while a>0:
    rev = rev * 10+ a % 10
    a=a//10

if rev ==copy:
    print("your number is a palindrome function")
else:
    print("not a palindrome number")