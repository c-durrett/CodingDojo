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
    
account1 = BankAccount(0.02 ,500)
account2 = BankAccount(0.01 ,0)

account1.deposit(100).deposit(100).deposit(100).withdrawal(150).yield_interest().display_account_info()
account2.deposit(10).deposit(20).withdrawal(10).withdrawal(10).withdrawal(5).withdrawal(6).yield_interest().display_account_info()

BankAccount.all_bank_accounts()