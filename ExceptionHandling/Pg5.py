a=int(input("enter the element a : "))
b=int(input("enter the element b : "))
try:
    c=a/b
    print(c)
except Exception as e:
    print(e.args)
finally:
    print("inside")