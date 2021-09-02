class Bank():
    name="SBI"
    def Account(self,Name,Number,Phone,Email):
        self.Name=Name
        self.Number=Number
        self.Phone=Phone
        self.Email=Email
        self.minimumbal= 2000
        self.balance=self.minimumbal
    def Deposit(self,amt):
        self.amt=amt
        self.balance = self.amt + self.balance
        print("your",Bank.name,"Account has Been Created With amount",self.amt)
        print("your current balance= ",self.balance)
    def Withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt > self.balance:
            print("insuffient Balance ! ")
        else:
            print("account debited with ",self.amnt)
            self.balance-=amnt
    