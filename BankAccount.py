class BankAccount:
    def __init__(self, account_holder:str, initial_balance:float):
        self.holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print("confirming the transfer ")

        else:
            print("error,not enough funds")

    def __str__(self):
        print(f"account holder: {self.holder},account balance: {self.balance} ")

