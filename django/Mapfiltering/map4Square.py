lst=[2,3,4,5,6]
# def square(num):
#     return num**2
# squares=list(map(square,lst))
# print(squares)
square=list(map(lambda num:num**2,lst))
print(square)