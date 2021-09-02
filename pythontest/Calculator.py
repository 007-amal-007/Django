def  add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
def expX(x,y):
    return x**y
def  expY(x,y):
    return y**x
    
while True:
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.exponent of fisrt element")
    print("6.exponent of 2nd element")
    x=int(input("enter the x value: "))
    y=int(input("enter the y value: "))
    choice=int(input("enter the choice : "))
    if (choice==1):
        print("the sum = ",add(x,y))
    elif (choice==2):
        print("the difference = ",sub(x,y))
    elif(choice==3):
        print("the multiplication =  ",mul(x,y))
    elif(choice==4):
        print("the division = ",div(x,y))
    elif(choice==5):
        print("the exponent of x= ",expX(x,y))
    elif(choice==6):
        print("the exponent of y= ",expY(x,y))
    else:
        print("invalid option")