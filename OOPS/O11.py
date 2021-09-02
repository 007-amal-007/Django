class Employee():
    company="hindhustan"
    def __init__(self,Id,name,role):
        self.Id=Id
        self.name=name
        self.role=role
    def printval(self):
        print("Emp Id: ",self.Id)
        print("Name : ",self.name)
        print("Role :",self.role)
        print(Employee.company)
obj=Employee(1,"Amal","Engineer")
obj.printval()