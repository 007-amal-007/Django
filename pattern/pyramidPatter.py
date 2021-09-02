n=int(input("enter the number : "))
for i in range(n):
    for j in range(n):
        print(end=" ")
    n=n-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()
         