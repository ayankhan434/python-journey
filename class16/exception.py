a = int(input(" enteer the first number : "))
b= int(input("enter the second number "))


try:
    print(a/b)
except Exception as err:
    print(f"sorry an error occured as {err}")

else:
    print("there bwas n error")



print(a+b)



