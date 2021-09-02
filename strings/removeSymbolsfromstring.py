punct="!@#$%^&*().';:\|/"
a=input("enter the string : ")
c=""
for char in a:
    if char not in punct:
        c= c+char
print(c)