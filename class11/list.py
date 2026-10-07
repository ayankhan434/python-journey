# list [you can store integer , float and even string ]

#list can also store duplicates

b=[11,22,33,33,33,33,22,22,22]

#list is mutable that meqan you can change anything

c=[1,2,3,4,5,6,7,7]

l= [10,20,30,40,50]

print(l[0],l[-5])

#slicing in list
print(l[:3])

a=["nature"]

a[0]='f'
#you cant change in the string

#deep copy and shallow copy

#shallow copy 
p=[1,2,3,4,5,6,7,8,9,87]

q=p.copy()

q[0]=1234567

print(q)
print(p)

#deep copy

#import copy



#travercing methood 1
j=[10,20,30,40,50]

for i in j:
    print(i)


for i in range(len(j)):
    print(j[i]) 


n=[10,20,30]
n.append(20)
print(n)
