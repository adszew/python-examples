class BankAccount:
    """
        Simple class representing a bank account supporting deposit,
        withdrawal, and statement generation.
    """
    def __init__(self, starting_balance=0):
        """
           Creates a new Monitor object with no configuration
        """
        self.balance = starting_balance

    def deposit(self, amount):
        """
           Adds money to the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        if (amount > self.balance):
            print("Insufficient funds")
        else:
            self.balance -= amount

    def display_balance(self):
        print("Balance ", self.balance)

if __name__ == '__main__':
    account = BankAccount(100)
    account.deposit(20)
    account.withdraw(40)
    account.withdraw(140)
    account.display_balance()
