n=int(input("enter the value of n : "))

even_sum=0;
odd_sum=0;

for i in range (1,n+1):
    if i%2==0:
        even_sum+=i;
    else:
        odd_sum+=i;
print(f"your odd sum is {odd_sum} and even sum is {even_sum}")