age = int(input("please tell your age : "))

#NOW We will choose can he vote or not in the upcoming election 

if age >= 18:
    print("hello , You Can Vote")

else: # You can't write any conditioon inside else
    print("hello , sorry You Can't vote")

if age>18:
    pass

else:
    print("can't pass")

# ammi paisa ee rhi hai 

money = int(input("please give me 10, 20, or 30 rs or above "))

if money ==10 :
    print("I Will Eat Choco Bar")

elif money >10 and money <=20:
    print("I will Eat mango Dolly")

elif money >20 and money <=30:
    print("I will Eat cone")
else:
    print("I will buy IceCream box")