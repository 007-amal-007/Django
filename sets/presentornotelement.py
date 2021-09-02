userIn = input("enter the element : ")
a="luminar"
flag=0
for i in a:
    if (i==userIn):
        flag=1
        break
    else:
        flag=0
if (flag==1):
    print("element is present")
else:
    print("element is not present")
