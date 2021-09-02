class Person():
    def set(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print("Name: ",self.name)
        print("rollno: ",self.rollno)
class Parent():
    def setv(self,div,School):
        self.div=div
        self.School=School
        print("Division: ",self.div)
        print("School: ",self.School)
class Teacher(Person,Parent):
    def PrintV(self,id,branch):
        self.id=id
        self.branch=branch
        print("Id: ",self.id)
        print("branch: ",self.branch)
te=Teacher()
te.set("amal",7)
te.setv("btech","CCE")
te.PrintV("CS2017007","Copmuter Science")