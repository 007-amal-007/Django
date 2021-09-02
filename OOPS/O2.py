class book():
    def details(self):
        print("The details of book")
        print("/****FLASH***SALE***/")
        print("BookName: Tales")
        print("Author: Amal")
        print("price: 100 Rs/-")
    def buy(self):
        p=int(input("enter 1 to buy"))
        if p==1:
            print("order placed")
B=book()
B.details()
B.buy()

B1=book()
B1.details()
B1.buy()