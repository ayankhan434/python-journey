#dictionary

d={"ayan":20,10:100,"dj":"bolller","amresh ":"best friend"}

d["ayan"]=200   #mutable can change the value but can't change the key

print(d["ayan"])   


d1=dict(name="ayan",age=20,vill="narwal")

print(d1)

d2=dict([("ayan","khan"),("age",20)])
d2.setdefault(20)

d2.update(d1)
print(d2)

a={1:10,2:20,3:30}

for i in a:
    print(a[i])