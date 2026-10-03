a=int(input("input the value of a :"))
b=int(input("input the value of b :"))
c=int(input("input the value of c :"))

if a>b and a>c:
    print(f" {a} is greater than {b} ,{c} ")
elif b>c and b>a:
    print(f" {b} is greater than {a} , {c}")
else:
    print(f"{c} is greater {b},{a} ")