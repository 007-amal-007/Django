lst=[1,2,3,4,5,6]
evens=list(filter(lambda num:num%2==0,lst))
print(evens)

odds=list(filter(lambda num:num%2!=0,lst))
print(odds)