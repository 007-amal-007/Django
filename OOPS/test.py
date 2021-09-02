class Animal:
    def __init__(self,name):
        self.name=name
    def printV(self):
        print(self.name)
obj=Animal("Dog")
obj.printV()