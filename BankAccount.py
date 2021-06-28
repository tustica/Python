class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance=balance
        if balance ==None:
            self.balance=0
        self.int_rate=.01
    
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdrawl(self, amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print("Balance: "+str(self.balance))
        return self
    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        print('Calculated interest is '+str(self.balance*self.int_rate))
        return self

myAccount = BankAccount(.01, 100)
myAccount.deposit(100).deposit(50).deposit(25).withdrawl(17).yield_interest().display_account_info()
    
bobsAccount = BankAccount(.01, 50)
bobsAccount.deposit(400).deposit(15000).withdrawl(3500).withdrawl(750).withdrawl(3000).yield_interest().display_account_info()