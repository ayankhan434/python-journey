a=[1,2,3,4,5,6,71,8,9,10]

max1=a[0]
max2=a[0]
index1=0
index2=0

for i in range(len(a)):
    if a[i]>max1:
        max2=max1
        max1=a[i]
       
        index2=index1
        index1=i
    elif a[i]>max2:
        max2=a[i]
        index2 = a[i]

print(f"max is {max1} at {index1} and sewc max is {max2} at {index2}")