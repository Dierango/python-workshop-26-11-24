class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return f"{amount} deposited successfully. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount}")
        return f"{amount} withdrawn successfully. Current balance: {self.balance}"

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def transaction(self):
        return self.transactions


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            return f"Account {account.account_number} already exists."
        self.accounts[account.account_number] = account
        return f"Account {account.account_number} added successfully."

    def get_account(self, account_number):
        return self.accounts.get(account_number, "Account not found.")


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        if customer.customer_id in self.customers:
            return f"Customer with ID {customer.customer_id} already exists."
        self.customers[customer.customer_id] = customer
        return f"Customer {customer.name} added successfully."

    def find_customer(self, customer_id):
        return self.customers.get(customer_id, "Customer not found.")

    def del_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            return f"Customer with ID {customer_id} deleted successfully."
        return "Customer not found."


if __name__ == "__main__":

    my_bank = Bank("My Bank")

    customer1 = Customer(101, input("Enter your name: "))

    print(my_bank.add_customer(customer1))

    account1 = Account(1001) 

    print(customer1.add_account(account1))

    print(account1.deposit(int(input("How much would you like to deposit: "))))
    print(account1.withdraw(int(input("How much would you like to withdraw: "))))
    print(account1.get_balance())

    print(account1.transaction())

    print(my_bank.find_customer(101))

    print(my_bank.del_customer(101))
    print(my_bank.find_customer(101))
