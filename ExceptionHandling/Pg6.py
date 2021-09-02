a=int(input("enter the element a: "))
b=int(input("enter the element b: "))
if b>a:
    raise Exception("n is greater than a ")
else:
    print(a/b)