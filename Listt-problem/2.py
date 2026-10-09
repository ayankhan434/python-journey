a=[1,2,3,4,54,65,76,87]

max=a[0]
index=0

for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        index=i


print(f"max is {max} and index is {index}")
