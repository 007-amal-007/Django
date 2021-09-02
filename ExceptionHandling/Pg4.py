l=[1,2,3,4]
u=int(input("enter the index : "))
try:
    print(l[u])
except Exception as e:
    print(e.args)
finally:
    print("inside")