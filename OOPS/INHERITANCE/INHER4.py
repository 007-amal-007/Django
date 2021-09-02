class Person():
    def set(self,name,age):
        self.name=name
        self.age=age
        print("Name :",self.name)
        print("Age :",self.age)
class Parent():
    def setv(self,Address,position):
        self.Address=Address
        self.position=position
        print("Adress :",self.Address)
        print("position :",self.position)
class Employee(Person,Parent):
    def Setva(self,id,cname):
        self.id=id
        self.cname=cname
        print("employee Id:",self.id)
        print("company name:",self.cname)
emp=Employee()
emp.set("amal",23)
emp.setv("jsnjsndjk","engineer")
emp.Setva("EMP101","Tariaq")       