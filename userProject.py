from BankAccount import BankAccount
class BankAccount:
    def __init__(self, int_rate, c_balance, s_balance):
        self.c_balance=c_balance
        self.s_balance=s_balance
        if c_balance or s_balance ==None:
            self.balance=0
        self.int_rate=.01
    
    def deposit_checking(self, amount):
        self.c_balance+=amount
        return self
    def deposit_savings(self, amount):
        self.s_balance+=amount
        return self
    def withdrawl_checking(self, amount):
        self.c_balance-=amount
        return self
    def withdrawl_savings(self, amount):
        self.s_balance-=amount
        return self
    def display_account_info(self):
        print("Balance: "+str(self.balance))
        return self
    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        print('Calculated interest is '+str(self.balance*self.int_rate))
        return self

# myAccount = BankAccount(.01, 100)
# myAccount.deposit(100).deposit(50).deposit(25).withdrawl(17).yield_interest().display_account_info()
# print(type(myAccount))
# bobsAccount = BankAccount(.01, 50)
# bobsAccount.deposit(400).deposit(15000).withdrawl(3500).withdrawl(750).withdrawl(3000).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.02, 0, 0)
    #add deposit method
    def deposit_checking(self, amount):
        self.account.c_balance+= amount
        return self
    def deposit_savings(self, amount):
        self.account.s_balance+= amount
        return self
    #make withdrawl
    def withdrawl_checking(self, amount):
        self.account.c_balance-=amount
        return self
    def withdrawl_savings(self, amount):
        self.account.s_balance-=amount
        return self
    #print name and account balance
    def info(self):
        print("Name: "+self.name)
        print("Balance for checking is "+str(self.account.c_balance)+' and for savings is '+str(self.account.s_balance))
    #transfer money to other user's account
    def transfer(self, other_user, amount):
        self.account.c_balance-=amount
        other_user.account.c_balance+=amount
    def display_balance(self):
        return ("Balance for checking is "+str(self.account.c_balance)+' and for savings is '+str(self.account.s_balance))

guido = User("Guido", "guido@gmail.com")
monty = User("Monty", "monty@gmail.com")
bob = User("Bob", "bob@email.com")
print(guido.name)

guido.deposit_checking(100).withdrawl_checking(30).deposit_savings(500).display_balance()
guido.info()

guido.transfer(monty, 11000)
monty.info()
guido.info()

monty.deposit_savings(200).deposit_checking(500).deposit_savings(1000).withdrawl_savings(1500).display_balance()
monty.info()