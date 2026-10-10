a = [12,13,15,23,24,25,29]

target =29

start =0
last = len(a)-1
mid = (start +last)//2


while start<=last:
    if a[mid]==target:
        print(f"element found at index { mid }")
        break
    elif a[mid]<target:
        start=mid+1
        mid=(start+last)//2

    elif a[mid]>target:
        last=mid-1
        mid=(start+last)//2

else:
    print("sorry no such element exist ")