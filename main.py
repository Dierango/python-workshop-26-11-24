import bank
import customer
import account
import random
from customer import Customer
from account import Account

def create_bank():
    bank_name = input("Enter the name of the bank: ")
    return bank.Bank(bank_name)

def create_customer(my_bank):
    ran_id = random.randint(1001, 9999)
    while ran_id in my_bank.customers:
        ran_id = random.randint(1001, 9999)
    customer_id = ran_id
    customer_name = input("Enter the customer name: ")
    c = customer.Customer(customer_id, customer_name)
    result = my_bank.add_customer(c)
    print(f"Created customer with ID: {customer_id}")
    print(result)
    return c

def create_account(my_bank, customer_id):
    customer = my_bank.find_customer(customer_id)
    if isinstance(customer, Customer):
        customer = my_bank.find_customer(customer_id)
        if customer.accounts != {}:
            new_account_number = max(customer.accounts.keys()) + 1
        else:
            new_account_number = 1001
        
        a = account.Account(new_account_number)
        result = customer.add_account(a)
        print(result)
        return a
    else:
        print(f"Customer with ID {customer_id} not found.")
        return None
def display_all_customers(my_bank):
    if not my_bank.customers:
        print("\nNo customers in the bank.")
        return
    
    print("\n=== Current Customers ===")
    for cust_id, customer in my_bank.customers.items():
        print(f"\nCustomer ID: {cust_id} | Name: {customer.name}")
        if not customer.accounts:
            print("  No accounts")
        else:
            print("  Accounts:")
            for acc_num, account in customer.accounts.items():
                print(f"    Account #{acc_num} | Balance: ${account.balance:.2f}")
    print("=====================")
def display_all_balances(my_bank):
    if not my_bank.customers:
        print("\nNo customers in the bank.")
        return
    
    all_accounts = []
    for cust_id, customer in my_bank.customers.items():
        for acc_num, account in customer.accounts.items():
            all_accounts.append({
                'customer_id': cust_id,
                'customer_name': customer.name,
                'account_number': acc_num,
                'balance': account.balance
            })
    
    # Sort by balance in descending order
    sorted_accounts = sorted(all_accounts, key=lambda x: x['balance'], reverse=True)
    
    print("\n=== All Account Balances (Descending Order) ===")
    for acc in sorted_accounts:
        print(f"Customer: {acc['customer_name']} (ID: {acc['customer_id']}) | Account #{acc['account_number']} | Balance: ${acc['balance']:.2f}")
    print("=====================")
def display_customer_balances(my_bank, customer_id):
    customer = my_bank.find_customer(customer_id)
    if isinstance(customer, Customer):
        if not customer.accounts:
            print("No accounts found for this customer.")
            return
        print(f"\n=== Account Balances for Customer: {customer.name} ===")
        sorted_accounts = sorted(customer.accounts.items(), key=lambda x: x[1].balance, reverse=True)
        for acc_num, account in sorted_accounts:
            print(f"Account #{acc_num} | Balance: ${account.balance:.2f}")
        print("=====================")
    else:
        print("Customer not found.")
def display_all_transactions(my_bank):
    all_transactions = []
    for customer in my_bank.customers.values():
        for account in customer.accounts.values():
            for transaction in account.transactions:
                all_transactions.append({
                    'customer_name': customer.name,
                    'account_number': account.account_number,
                    'transaction': transaction
                })
    
    # Sort by timestamp (assuming timestamp is at the start of transaction string)
    sorted_transactions = sorted(all_transactions, key=lambda x: x['transaction'], reverse=True)
    
    print("\n=== All Transactions (Most Recent First) ===")
    for trans in sorted_transactions:
        print(f"{trans['customer_name']} - Account #{trans['account_number']}: {trans['transaction']}")
    print("=====================")


def main():
    while True:
        print("\n=== Banking System ===")
        print("1. Start a bank")
        print("2. Exit")
        
        pre_choice = input("Enter your choice (1-2): ")
        
        if pre_choice == '1':
            my_bank = create_bank()
            
            while True:
                print("\n1. Create new customer")
                print("2. Create account for existing customer")
                print("3. Make deposit")
                print("4. Make withdrawal")
                print("5. Check balance")
                print("6. View transactions")
                print("7. List all customers")
                print("8. Return to main menu")
                
                
                
                choice = input("Enter your choice (1-8): ")
                
                if choice == '1':
                    customer1 = create_customer(my_bank)
                    print(f"Your customer ID is: {customer1.customer_id}")
                
                elif choice == '2':
                    customer_id = int(input("Enter customer ID: "))
                    account1 = create_account(my_bank, customer_id)
                
                elif choice == '3':
                    customer_id = int(input("Enter customer ID: "))
                    account_number = int(input("Enter account number: "))
                    customer = my_bank.find_customer(customer_id)
                    if isinstance(customer, Customer):
                        account = customer.get_account(account_number)
                        if isinstance(account, Account):
                            amount = float(input("Enter deposit amount: "))
                            print(account.deposit(amount))
                
                elif choice == '4':
                    customer_id = int(input("Enter customer ID: "))
                    account_number = int(input("Enter account number: "))
                    customer = my_bank.find_customer(customer_id)
                    if isinstance(customer, Customer):
                        account = customer.get_account(account_number)
                        if isinstance(account, Account):
                            amount = float(input("Enter withdrawal amount: "))
                            print(account.withdraw(amount))
                
                elif choice == '5':
                    print("\n1. View all account balances")
                    print("2. Check specific customer's balances")
                    balance_choice = input("Enter your choice (1-2): ")
                    
                    if balance_choice == '1':
                        display_all_balances(my_bank)
                    elif balance_choice == '2':
                        customer_id = int(input("Enter customer ID: "))
                        display_customer_balances(my_bank, customer_id)

                
                elif choice == '6':
                    print("\n1. View all transactions")
                    print("2. View specific customer's transactions")
                    inner_choice = input("Enter your choice (1-2): ")
                    
                    if inner_choice == '1':
                        display_all_transactions(my_bank)
                    elif inner_choice == '2':
                        customer_id = int(input("Enter customer ID: "))
                        customer = my_bank.find_customer(customer_id)
                        if isinstance(customer, Customer):
                            print(f"\n=== Transactions for Customer: {customer.name} ===")
                            for acc_num, account in customer.accounts.items():
                                print(f"\nAccount #{acc_num}:")
                                if account.transactions:
                                    for transaction in reversed(account.transactions):
                                        print(transaction)
                                else:
                                    print("No transactions")
                            print("=====================")
                        else:
                            print("Customer not found.")
                
                elif choice == '7':
                    display_all_customers(my_bank)
                elif choice == '8':
                    break
        elif pre_choice == '2':
            print("Thank you for using the banking system!")
            break                 

if __name__ == "__main__":
    main()
    
        