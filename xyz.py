class car:
    def cardet(self):
        self.cnumber=int(input("Car No.? "))
        self.ccompany=input("Company: ")
        self.cmodel=input("Model: ")
        self.cprice=int(input("Price: "))
    def showcardet(self):
        print(self.cnumber)
        print(self.ccompany)
        print(self.cmodel)
        print(self.cprice)
