class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "account1" : BankAccount(0.02, 500),
            "account2" : BankAccount(0.01, 0)
        }

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(f"User:{self.name}, Balance: ${self.account}")
        return self

    def transfer_money(self, amount, user):
        self.account -= amount
        user.account += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

    # def example_method(self):
    #     self.account.deposit(100)
    #     print(self.account.balance)


class BankAccount:
    # int_rate = 0.01
    # balance = 0
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance-5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def all_bank_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


sean = User("Sean van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bryce = User("Bryce Fly", "marty@python.com")

adrien = User("Adrien", "adrien@dojo.com")
adrien.account['account1'].deposit(100)
adrien.display_user_balance()
sean.display_user_balance()

# sean.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(500).display_user_balance()

# monty.make_deposit(200).make_deposit(300).make_withdrawal(50).make_withdrawal(50).display_user_balance()

# bryce.make_deposit(1000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(600).display_user_balance()

# sean.transfer_money(100, bryce)