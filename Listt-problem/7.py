a = [10,20,30,40,50]

b = len(a)-1

for i in range (len(a)//2):
    a[i],a[b]=a[b],a[i]
    b=b-1

print (a)