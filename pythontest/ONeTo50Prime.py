def O1To50(x,y):
    for p in range(x,y+1):
        if p>1:
            for i in range(2,p):
                if p%i==0:
                    break
            else:
                print(p)
O1To50(1,50)