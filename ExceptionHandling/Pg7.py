age=int(input("enter the  age : "))
if age<18:
    raise Exception("Vaccination is not Possible ! ")
else:
    print("possible for Vaccination")