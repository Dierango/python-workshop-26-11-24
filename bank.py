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
