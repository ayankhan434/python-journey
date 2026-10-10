a = [1,2,3,4,5,6,7,8,9,23]


target =6
for i in range(len(a)):
    if a[i]==target:
        print(f"element is found at index {i}")
        break;
else:
    print("sorry no such element found ")

    