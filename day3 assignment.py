class BankAccount:
    def myacc(self):
        print(f"the accountnumber = {self.accountnumber}")
        print(f"the balance of the account = {self.balance}")

    def getdepositbalance(self):
        self.accountnumber = int(input("enter the accountnumber = "))
        self.deposit = int(input("enter the deposit amt = "))
        self.withdraw = int(input("enter the withdraw amt = "))
        self.balance = self.deposit - self.withdraw


d1 = BankAccount()
d1.getdepositbalance()
d1.myacc()
print("-------------")
d2 = BankAccount()
d2.getdepositbalance()
d2.myacc()
