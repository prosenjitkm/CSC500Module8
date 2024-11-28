# Define a class for a bank account
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.balance = balance  # Public attribute

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

# Create instances of the class
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Access attributes and methods for account1
print(f"Account Holder: {account1.account_holder}, Balance: ${account1.balance}")
account1.deposit(200)

# Access attributes and methods for account2
print(f"Account Holder: {account2.account_holder}, Balance: ${account2.balance}")
account2.deposit(300)
