l1=[1,2,3,4,5,6,7,9,11,22,33,44,55,66,77,88,99]
flag=0
User=int(input("enter the elements to be searched : "))
for i in l1:
    if User==i:
        flag=1
        break
if flag==1:
    print("element is found")
else:
    print("element is not found")