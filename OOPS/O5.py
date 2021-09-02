class Sum():
    def Setval(self, x, y):
        self.x=x
        self.y=y
    def disVal(self):
        print("res",self.x + self.y)
sm= Sum()
sm.Setval(2,3)
# x=int(input("enter the x value : "))
# y=int(input("enter the y value : "))
sm.disVal()
