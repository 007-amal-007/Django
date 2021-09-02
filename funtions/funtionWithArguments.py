def facto(num):
    if num>0:
        f=1
        for i in range(1,num+1):
            f=f*i
        print(f)
    elif num<0:
        print("factorial is couldnt get , it is a negative number ! ")
    elif num==0:
        print("factorial is 1 ")
facto(5)
facto(0)
facto(6)
facto(-1)

#uisng return
# def facto(num):
#     if num>0:
#         f=1
#         for i in range(1,num+1):
#             f=f*i
#             return f
#     elif num<0:
#         return("factorial is couldnt get , it is a negative number ! ")
#     elif num==0:
#         return("factorial is 1 ")
# print(facto(5))
# print(facto(0))
# print(facto(6))
# print(facto(-1))
