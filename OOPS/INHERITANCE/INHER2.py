class Person():
    def set(self,age,name,Adress):
        self.age=age
        self.name=name
        self.Adress=Adress
        print(self.name,self.age,self.Adress)
class Employee(Person):
    def printval(self,id,salary,dept):
        self.id=id
        self.salary=salary
        self.dept=dept
        print(self.id,self.salary,self.dept)
emp=Employee()
emp.set("amal",23,"abcdefghi")
emp.printval(2,45000,"development")