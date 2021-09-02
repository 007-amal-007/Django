class Registraion():
    def UserReg(self,name,email,password,Age,PhoneNumber):
        self.name=name
        self.email=email
        self.password=password
        self.Age=Age
        self.PhoneNumber=PhoneNumber
    def DisplayUser(self):
        print("name : ",self.name)
        print("email : ",self.email)
        print("password : ",self.password)
        print("Age : ",self.Age)
        print("Phone Number : ",self.PhoneNumber)
us=Registraion()
us.UserReg("Amal","Amalsankarps0@gmail.com","*******",24,"9656214124")
us.DisplayUser()