l=[-1,-3,-5,0,-9,9,-8,7,6,5]
l1=[]
while l:
    min = l[0]
    for i in l:
        if i <  min:
            min = i
    l1.append(min)
    l.remove(min)
print(l1)
print(l)