import random

num = random.randint(1,100)

tries=0

while True:

    guessed= int (input("guess the number btw 1 to 100 : "))
    tries+=1
  

    if guessed==num:
        print(f"congo you found the num {num} in {tries} attempt")
        break
    elif guessed>num:
        print("you need to go lower number")
    elif guessed<num:
        print("you need to go upper number")