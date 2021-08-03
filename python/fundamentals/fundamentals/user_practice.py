class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User:{self.name}, Balance: ${self.account_balance}")
    
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
marty = User("Marty Fly", "marty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(500)
guido.display_user_balance()

monty.make_deposit(200)
monty.make_deposit(300)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
monty.display_user_balance()

marty.make_deposit(1000)
marty.make_withdrawal(200)
marty.make_withdrawal(200)
marty.make_withdrawal(600)
marty.display_user_balance()

guido.transfer_money(100, marty)