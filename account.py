from datetime import datetime

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        self.balance += amount
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"[{timestamp}] Deposited: ${amount:.2f}")
        return f"{amount} deposited successfully. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"[{timestamp}] Withdrawn: ${amount:.2f}")
        return f"{amount} withdrawn successfully. Current balance: {self.balance}"

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def transaction(self):
        return self.transactions