l=[1,2,3]
u=int(input("enter the index value : "))
try: 
    print(l[u])
except:
    print("out of range ! ")
finally:
    print("final statement")