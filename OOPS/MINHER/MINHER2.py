class Student:
    def StudentId(self,rollno,branch):
        self.rollno=rollno
        self.branch=branch
        print("rollno: ",self.rollno)
        print("branch: ",self.branch)
class Child(Student):
    def ChildSub(self,subject,grade):
        self.subject=subject
        self.grade=grade
        print("Subject is: ",self.subject)
        print("Grade is: ",self.grade)
class Pearson(Child):
    def Pearson(self,name,gender):
        self.name=name
        self.gender=gender
        print("name is:",self.name)
        print("gender is",self.gender)
p=Pearson()
p.StudentId(1,"computer science")
p.ChildSub("TOC","C")
p.Pearson("Amal","Male")
