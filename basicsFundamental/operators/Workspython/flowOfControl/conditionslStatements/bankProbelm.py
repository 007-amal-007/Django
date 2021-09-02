userIn = int(input("enter the withdraw amount : "))
FixedUserAmount = 10000
if userIn <= FixedUserAmount:
    print('Successfully withdraw Rs= ',userIn)
    print('balance',FixedUserAmount-userIn)
else:
    print("you have insuficient amount cash")