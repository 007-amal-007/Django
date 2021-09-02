min = int(input("enter the min range: "))
max = int(input("enter the max range: "))
print("---------evennumbers----------")
for i in range (min,max+1):
    if (i%2==0):
        print(i)