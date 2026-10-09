k = int(input("how many time you want to rotate : "))
a=[10,20,30,40,50]

for i in range(k):
    for i in range(len(a)-1):
        a[i],a[i+1]=a[i+1],a[i]


print(a)