def add(a,b):
    print(a+b)

add(11,12)
add(23,34)

def is_palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return original == rev


num = int(input("Enter number: "))

if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")