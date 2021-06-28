class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    #add deposit method
    def deposit(self, amount):
        self.account_balance += amount
        return self
    #make withdrawl
    def withdrawl(self, amount):
        self.account_balance-=amount
        return self
    #print name and account balance
    def info(self):
        print("Name: "+self.name)
        print("Balance: "+str(self.account_balance))
    #transfer money to other user's account
    def transfer(self, other_user, amount):
        self.account_balance-=amount
        other_user.account_balance+=amount
    def display_balance(self):
        return ("Balance: "+str(self.account_balance))

guido = User("Guido", "guido@gmail.com")
monty = User("Monty", "monty@gmail.com")
bob = User("Bob", "bob@email.com")
print(guido.name)

guido.deposit(100).withdrawl(30).deposit(500).display_balance()
guido.info()

guido.transfer(monty, 100)
monty.info()
guido.info()

monty.deposit(200).deposit(500).deposit(1000).withdrawl(1500).display_balance()
monty.info()