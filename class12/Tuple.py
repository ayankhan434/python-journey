#tuple 

a=(1,2,3,4,5,6,8)

#tuple has hetrogenous nature

#tuple has a immutable nature

#tuple can store duplicate values

#tuple unpacking

a,b,c=(10,20,30)

print(b)


a = (10,20,30,40)

print(a[3])


b=[1,2,3,4,5]

tup = tuple(b)

print(tup)


t=(10,20,30,40,50)

#1st way

for i in t:
    print(i)


#2nd way

for i in range(len(t)):
    print(t[i])


#tuple methoods

#help(tuple)

a=(1,1,1,1,1,3,4)

print(a.count(1))
print(a.index(1))