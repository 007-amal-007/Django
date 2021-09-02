que=[]
size=int(input("enter the queue size : "))
front=0
rear=0
n=0
def enqueue():
    global front,rear,size,que
    if(que > size):
        print("Queue is full")
    else:
        p=int(input("enter the elements to the queue"))
        que.insert(rear, p)
        rear+=1

        for i in range(front,rear):
            print(que[i])
def dequeue():
    global front,rear,size,que
    if (rear == front):
        print("queue is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while (n!=1):
    print("enter the option you want to perform : ")
    choice=int(input("enter the option : 1.enqueu 2.dequeue"))
    if (choice==1):
        enqueue()
    elif (choice==2):
        dequeue()
    