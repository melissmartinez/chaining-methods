class User:
    def __init__(self, nm, em):
        self.name = nm
        self.email = em
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def withdrew(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfered_funds(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

guido = User("Guido van Rossum", "guido@email.com")
monty = User("Monty Python", "monty@email.com")
melissa = User("Melissa Martinez", "mmartinez@email.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).withdrew(400).display_user_balance()

monty.make_deposit(50).make_deposit(150).withdrew(25).withdrew(15).display_user_balance()

melissa.make_deposit(500).withdrew(50).withdrew(50).withdrew(50).display_user_balance()

melissa.transfered_funds(monty, 100)