class bank():
    def __init__(self,accno,name,type,balance):
        self.accno=accno
        self.name=name
        self.type=type
        self.balance=balance
    def deposit(self,accno):
        self.balance+=accno
        print("After deposit balance amount",self.balance)
    def withdraw(self,accno):
        self.balance-=accno
        print("After withdraw balance", self.balance)
accno=int(input("Enter the account no:"))
name=input("Enter the name:")
type=input("Enter the type of account:")
balance=int(input("Enter the balance:"))
obj=bank(accno,name,type,balance)
d=int(input("Enter the amount to be deposit:"))
obj.deposit(d)
w=int(input("Enter the amount to be withdraw:"))
obj.withdraw(w)