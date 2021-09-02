studentName = (input('enter the student name '))
m1 = int(input("enter the mark1 "))
m2 = int(input("enter the mark2 "))
m3 = int(input("enter the mark3 "))
m4 = int(input("enter the mark4 "))
m5 = int(input("enter the mark5 "))
totalMark = m1 + m2 + m3 + m4 + m5
averageScore = totalMark / 5
print(studentName,'\n','----------------')
print('total score = ',totalMark)
print('average score  = ',averageScore,'\n','--------------')