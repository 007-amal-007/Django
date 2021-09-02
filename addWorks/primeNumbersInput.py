minimum = int(input("enter the minimum range : "))
maximum =  int(input("enter the maximum range : "))
for p in range(minimum,maximum+1):
    if p>1:
        for i in range(2,p):
            if p%i==0:
                break
        else:
            print(p)
