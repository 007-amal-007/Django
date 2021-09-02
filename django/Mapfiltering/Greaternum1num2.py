from functools import reduce
lst=[2,3,4,5,6]
loow=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(loow)