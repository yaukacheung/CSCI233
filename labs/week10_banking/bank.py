
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False

        self.balance += amount
        print(f"${amount:.2f} deposited successfully into {self.owner}'s account.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
            return False

        self.balance -= amount
        print(f"${amount:.2f} withdrawn successfully from {self.owner}'s account.")
        return True

    def display_balance(self):
        print(f"{self.owner}'s account balance: ${self.balance:.2f}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create two different account objects
    account1 = BankAccount("Alice", 500)
    account2 = BankAccount("Bob", 300)

    # Alice's transactions
    print("--- Alice's Account ---")
    account1.display_balance()
    account1.deposit(200)
    account1.withdraw(100)
    account1.withdraw(1000)  # Insufficient funds
    account1.display_balance()

    # Bob's transactions
    print("\n--- Bob's Account ---")
    account2.display_balance()
    account2.deposit(150)
    account2.withdraw(50)
    account2.display_balance()
