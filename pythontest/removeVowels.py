vowels="aeiou"
c=""
usp=input("enter the string: ")
for i in usp:
    if i not in vowels:
        c=c+i
print(c)