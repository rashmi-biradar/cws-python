"""
Bank
    New objec create (constructor)
        account=0
        account_no =randomly
        name_input
        bank_name
    Withdraw
    Deposit
    Display
    DisplayBalance
    Update
obj
        
"""
# import random


# class Bank:
#     def __init__(self):
#         self.amount = 0
#         self.accno = random.randint(100000, 999999)
#         self.name = input("enter your name = ")
#         self.bankName = input("enter your bank name = ")

#     def display(self):
#         print(f"/n-----------INFO-----------")
#         print(f"Account number ={self.accno}")
#         print(f"Balance ={self.amount}")
#         print(f"Name ={self.name}")
#         print(f"Bank name ={self.bankName}")

#     def displayBalance(self):
#         print(f"your balance ={self.amount}")

# def deposit(self):
#     newAmount = int(input("enter the amount to deposit = "))
#     self.amount = self.amount + newAmount
#     self.displayBalance()

# def withdraw(self):
#     newAmount = int(input("enter amount to withdraw = "))
#     if newAmount > self.amount:
#         print(f"insufficient balance. your actual balance is {self.amount}")
#     else:
#         self.amount = self.amount - newAmount
#         self.displayBalance()

#     def update(self):
#         newBankName = input("enter new name. or if you want default leave blank = ")
#         if newBankName != "":
#             self.bankName = newBankName


# obj = Bank()
# obj.display()
# obj.deposit()
# obj.withdraw()
# obj.update()
# obj.display()


# class Book:
#     def __init__(self):
#         self.title = input("enter the title = ")
#         self.author = input("enter the author name = ")
#         self.price = int(input("enter the price = "))

#     def discount(self):
#         print("/n----INFO----")
#         discamt = int(input("enter the discount amount = "))
#         discountamt = (self.price) * (discamt / 100)
#         newdiscamt = self.price - discountamt
#         print(f"the discounted price is {newdiscamt} ")


# obj = Book()
# obj.discount()
# print("------------")
# d = Book()
# d.discount()

# class Employee:
#     def __init__(self):
#         self.depart = input("enter the department name = ")
#         self.name = input("enter the name = ")
#         self.age = int(input("enter the age = "))
#         self.salary = int(input("enter the current salary = "))

#     def promote(self):
#         print("/n----INFO----")
#         increpercent = int(input("enter the increment percentage = "))
#         percent = (self.salary) * (increpercent / 100)
#         newincreamt = self.salary + percent
#         print(f"the incremented salary is  {newincreamt} ")


# obj = Employee()
# obj.promote()
# print("------------")
# d = Employee()
# d.promote()


class BankAccount:
    def __init__(self):
        self.accno = int(input("enter the account number = "))
        self.balance = int(input("enter the  balance amount = "))

    def deposit(self):
        newAmount = int(input("enter the amount to deposit = "))
        self.balance = self.balance + newAmount
        print(f"the balance after the deposit amount is {self.balance}")
        print("---------")

    def withdraw(self):
        newAmount = int(input("enter amount to withdraw = "))
        if newAmount > self.balance:
            print(f"insufficient balance. your actual balance is {self.balance}")
        else:
            self.balance = self.balance - newAmount
            print(f"your balance after the withdraw is {self.balance} ")


obj = BankAccount()
obj.deposit()
obj.withdraw()
