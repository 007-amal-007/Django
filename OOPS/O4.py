class employee():
    def Setvalue(self,employee_Id,employee_name,employe_role,employee_Age):
        self.employee_Id=employee_Id
        self.employee_name=employee_name
        self.employee_role=employe_role
        self.employee_Age=employee_Age
    def Printvalue(self):
        print("Id",self.employee_Id)
        print("Name",self.employee_name)
        print("Role",self.employee_role)
        print("Age",self.employee_Age)
EMP=employee()
EMP.Setvalue("EMP1","AmalSankar","Engineer",23)
EMP.Printvalue()

