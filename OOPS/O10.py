#constructor 
class Person():
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printval(self):
        print(self.name,self.age,self.address)
obj = Person("Amal",23,"payathuparambil House")
obj.printval()