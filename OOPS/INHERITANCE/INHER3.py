class Person():
    def set(self,name,age):
        self.name=name
        self.age=age
        print("name: ",self.name)
        print("Age is : ",self.age)
class Child():
    def setv(self,id,adres):
        self.id=id
        self.adres=adres
        print("name: ",self.id)
        print("Adress is : ",self.adres)
class Student(Person,Child):
    def printS(self,std,school):
        self.std=std
        self.school=school
        print("Std :",self.std)
        print("school",self.school)
st=Student()
st.set("Amal",23)
st.setv(2017007,"abcd")
st.printS("UG","CNN BHS SCHOOL")