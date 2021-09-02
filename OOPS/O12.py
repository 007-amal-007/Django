class Calculator():
    def __init__(self,a,b):
        self.x=x
        self.y=y
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y 
x=int(input("enter the number x: "))
y=int(input("enter the number y: "))
cal=Calculator(x,y)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
