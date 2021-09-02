# list=[1,2,3,4,5,6]
# min=0
# for i in list:
#     min=i
#     i=i+1
#     if min > i+1:
#         min=i
#         i=i+1
# print(i)

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second largest element is:",a[n-2])