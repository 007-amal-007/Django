stk=[]
size=int(input("enter the size of the stack : "))
top=0
n=0
def pushs():
    global top,size,stk
    if (top>size):
        print("stack is full")
    else:
        p=int(input("enter the elements to the stack : "))
        stk.append(p)
        top=top+1
def display():
    print(stk)
def pops():
    global top,size,stk
    if (top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top=top-1
while (n!=1):
    print("select the operation you want to perform : ")
    choice=int(input("1.push element, 2.pop ,3.display : "))
    if (choice==1):
        pushs()
    elif (choice==2):
        pops()
    elif (choice==3):
        display()
    n=int(input("do you wnat continue the operaation : "))