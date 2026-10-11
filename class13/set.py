s={1,2,34,456,666,"hello",(1,2,3)}

#you can only store hashable values inside set

print(hash("hello"))

#unordered nature

s={12,23234,5346,676543,3245,634,6745}

print(s)


#you can not have duplicate values
s={12,12,1221,12,23,34}
print(s)

# you cant target any numberor index here 

#set travercing
s={12,23,34,45,56,67,78}

for i in s:
    print(i)


s1={10,20,30,40}
s2={10,20,50,60}
print(s2 - s1)
print(s1 - s2)

s1.discard(10)

print(s1)

print(s1&s2)