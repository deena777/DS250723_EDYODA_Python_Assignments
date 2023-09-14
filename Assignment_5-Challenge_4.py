# Challenge 4 and Challenge 5 are both banking account related problems


# Challenge 4: Implement a Banking Account


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def set_account_info(self):
        self.title = input("Enter account title: ")
        self.balance = float(input("Enter account balance: "))

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=None):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def set_savings_account_info(self):
        super().set_account_info()
        self.interestRate = float(input("Enter interest rate: "))



print("\nAccount Information")
account = Account()
account.set_account_info()

print(f"Title: {account.title}")
print(f"Balance: {account.balance}")


print("\nSavings Account Information")
savings_account = SavingsAccount()
savings_account.set_savings_account_info()

print(f"Title: {savings_account.title}")
print(f"Balance: {savings_account.balance}")
print(f"Interest Rate: {savings_account.interestRate}\n")







# Challenge 5: Handling a Bank Account


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

SA = SavingsAccount()

SA.balance = float(input("Enter initial balance: "))
SA.interestRate = float(input("Enter interest rate (%): "))

withdrawal_amount = float(input("Enter withdrawal amount: "))
SA.withdrawal(withdrawal_amount)

deposit_amount = float(input("Enter deposit amount: "))
SA.deposit(deposit_amount)

print("Updated balance:", SA.getBalance())

interest = SA.interestAmount()
print("Interest amount:", interest)
