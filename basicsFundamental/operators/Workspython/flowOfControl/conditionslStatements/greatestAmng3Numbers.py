n1 = int(input("enter the number 1 "))
n2 = int(input("enter the number 2 "))
n3 = int(input("enter the number 3 "))
if n1>n2>n3 and n1>n3:
    print(n1,"is greater than ",n2,n3)
elif n2>n3:
    print(n2,"is greater than ",n1,n3)
elif n1==n2==n3:
    print("three numbers are equal")
else:
    print(n3,"is greater than ",n1,n2)
