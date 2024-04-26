#cam Robinson due: 3/29/24
import sys

class CheckingAccount:
    balance=0
    
    def __init__(self,b):
        self.balance=b
        print("This account is opened with $"+str(balance))
    def withdraw(self,asa):
        self.withdraw=self.balance-asa
        print("The balance after withdrawing $"+str(asa),"is $"+str(ca.withdraw))
    def deposit(self,nd):
        self.deposit=nd+self.withdraw
        print("The balance after depsoting $"+str(nd),"is $"+str(ca.deposit))
        
balance=int(sys.argv[1])
asa=int(sys.argv[2])
nd=int(sys.argv[3])

ca=CheckingAccount(balance)
ca.withdraw(asa)
ca.deposit(nd)