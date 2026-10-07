a = int(input("Enter the Number: "))

copy = a
square = a * a

while a > 0:
    if square % 10 != a % 10:
        print("Not an Automorphic Number")
        break

    a = a // 10
    square = square // 10

else:
    print("Automorphic Number")