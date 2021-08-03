class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User:{self.name}, Balance: ${self.account_balance}")
        return self
    
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

sean = User("Sean van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bryce = User("Bryce Fly", "marty@python.com")

sean.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(500).display_user_balance()

monty.make_deposit(200).make_deposit(300).make_withdrawal(50).make_withdrawal(50).display_user_balance()

bryce.make_deposit(1000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(600).display_user_balance()

sean.transfer_money(100, bryce)