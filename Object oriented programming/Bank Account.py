#Creating a bank account class
class BankAccount(object):
    #Creating the variables
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.pinNumber = 2468
        self.intRate = 0.06
        self.accNum = 1223456789
    def creditAcc(self):
        ammount = float(input("Enter your deposit"))
        self.balance+=ammount
    def debit(self):
        ammount = float(input("Enter your withdraw"))
        getPin = int(input("Enter your pin number: "))
        if getPin != self.pinNumber:
            print("That is incorrect WEE WOO THATS THE SOUND OF THE POLICE")
        else:
            self.balance-=ammount

jadeAcc = BankAccount()
jadeAcc.name = "Jade"
jadeAcc.creditAcc()
print(jadeAcc.balance)
jadeAcc.debit()
print(jadeAcc.balance)

