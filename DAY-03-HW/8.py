age=int(input("Enter the age : "))

if age%100==0 and age%400==0:
   print(f"{age} is a leap year")
else:
   print(f"{age} is not a leap year ")