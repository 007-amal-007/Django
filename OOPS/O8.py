class Employee():
    Company="Luminar Tech"
    def Setval(self,Id,Name,Gender,Role):
        self.Id=Id
        self.Name=Name
        self.Gender=Gender
        self.Role=Role
    def Disval(self):
        print("Roll No : ",self.Id)
        print("Name : ",self.Name)
        print("Gender : ",self.Gender)
        print("Role : ",self.Role)
        print(Employee.Company)
Emp=Employee()
Emp.Setval(1,"Amal","Male","Engineer")
Emp.Disval()