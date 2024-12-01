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