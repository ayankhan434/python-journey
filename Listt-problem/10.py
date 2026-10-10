#bubble short

a = [12345,1,2,3,4,5,54,36,4645]

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]




print(a)