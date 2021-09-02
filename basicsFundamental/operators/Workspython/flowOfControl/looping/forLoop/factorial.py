num = int(input("enter the numner "))
fact=1
if num>0:
    for i in range (fact,num+1):
        fact = fact *i
    print(fact)
if num==0:
    print("factorial of 0 is 1 ")
elif num<0:
    print("negative number")
