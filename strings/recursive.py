a=input("enter the elements : ")
c=""
for i in a:
    if i not in c:
        c=c+i
    else:
        print("the repeating characters in ",a," is ",i)