class Account:
    def __init__(self, name: str, balance: float):
        self._name = name
        self._balance = balance
        if balance < 0.0:
            self._balance = 0.0

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount

    def withdraw(self, withdraw_amount: float):
        if withdraw_amount < self._balance:
            print("Insufficient funds for withdrawal.")
        elif withdraw_amount > 0:
            self._balance -= withdraw_amount
    def get_balance(self) -> float:
        return self._balance
    def set_name(self, name: str):
        self._name = name
    def get_name(self) -> str:
        return self._name
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdrawal amount exceeded account balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
def __str__(self):
        return f"Account Title: {self.__account_title}\nBalance: ${self.__balance:.2f}"
__name__ == "__main__":
    account1 = Account("Kashif", 100.0)
    print("--- Initial Account State ---")
    print(account1)
    print()

    print("Depositing $50...")
    account1.deposit(50.0)
    print(f"Updated Balance: ${account1.get_balance():.2f}\n")

    print("Withdrawing $30...")
    account1.withdraw(30.0)
    print(f"Updated Balance: ${account1.get_balance():.2f}\n")

    print("Attempting to withdraw $200 (Exceeds balance)...")
    account1.withdraw(200.0)