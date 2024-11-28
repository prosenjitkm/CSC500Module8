# Define a class for a bank account with a private balance attribute
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance  # Getter method for the private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"${amount} deposited. New balance: ${self.__balance}")

# Create an instance of the class
account = BankAccount("Alice", 1000)

# Access the public attribute
print(f"Account Holder: {account.account_holder}")

# Access the private attribute using a getter method
print(f"Balance: ${account.get_balance()}")

# Modify the private attribute using a method
account.deposit(200)

# Attempting to access the private attribute directly results in an error
# Uncommenting the line below will raise an AttributeError
print(account.__balance)
