def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y

print("select the operation")
print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
while True:
    ec = int(input("enter the choice : "))
    n1 = int(input("enter the number 1 : "))
    n2 = int(input("enter the number 2 : "))
    if ec==1:
        print(add(n1,n2))
    elif ec==2:
        print(sub(n1,n2))
    elif ec==3:
        print(mul(n1,n2))
    elif ec==4:
        print(div(n1,n2))
    else:
        print("invalid choice")

