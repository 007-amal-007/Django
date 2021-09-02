class Student():
    def SetVal(self,Id,Name,Age,Gender,school):
        self.Id=Id
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.school=school
    def DisVal(self):
        print("Roll No : ",self.Id)
        print("Name : ",self.Name)
        print("Age : ",self.Age)
        print("Gender : ",self.Gender)
        print("School Name : ",self.school)
s=Student()
s.SetVal(1,"Amal",23,"Male","Cnn Bhs Cherpu")
s.DisVal()