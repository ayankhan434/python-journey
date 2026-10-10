#selection sort

a=[123,23,34,45,56,67,78,79]

for i in range (len(a)-1):
    j = i+1
    min = i
    for k in range (j,len(a)):
        if a [k] < a[min]:
            min = k

    a[i],a[min]=a[min],a[i]


print(a)