# add all the possible factors of a number

n= int(input(" enter the value of n: "))

sum=0;

for i in range (1, n+1):
    if n%i==0:
        sum=sum+i;

print(f"the sum is {sum}")


