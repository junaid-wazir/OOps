# # class Account:
# #     def __init__(self, account_title, balance=0):
# #         self.__account_title = account_title
# #         self.__balance = balance
# #         def setbalance()
# #     def show(self):
# #         return(f"Account Title: {self.__account_title}, Balance: {self.__balance}")

# class Account:
#     def __init__(self, account_title, balance=0):
#         self.__account_title = account_title
#         self.__balance = balance

#     def setbalance(self, balance):
#         if balance < 0:
#             print("Balance cannot be negative.")
#         Account.
#         self.__balance = balance

#     def show(self):
#         return(f"Account Title: {self.__account_title}, Balance: {self.__balance}")

class Account:
    def __init__(self,name: str, balance: float):
        self.__account_title = name
        if balance >= 0:
            self.__balance = balance

    def setBalance(self,balance: float):
        if balance >= 0:
            self.__balance = balance

    def getBalance(self) -> float:
        return self.__balance

    def setAccountTitle(self,account_title: str):
        self.__account_title = account_title

    def getAccountTitle(self) -> str:
        return self.__account_title

    def withdraw(self,amount: float):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
        


    def __str__(self):
        return f"Account Title: {self.__account_title}\nBalance: {self.__balance:.2f}"

account1 = Account("Kashif", 1000.0)
print(account1)

print(account3.getBalance())