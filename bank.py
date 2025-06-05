print("---- practice with Encapsulation ----")
class BankAccount:
    def __init__(self, balance):

        self.__balance = balance
    def deposit(self, amount):
        self.amount = amount
        self.__balance += self.amount
        return f"➕🏧you deposit {self.amount} € in your account, your balance is:{self.__balance} €"

    def withdraw(self, amount):
        self.amount = amount
        if amount < self.__balance:
            self.__balance -= self.amount
            return f"➖🏧you withdraw {self.amount} € your account, your balance is: {self.__balance} €"
        else:
            return "🤷‍♂️you have not enough balance!"


    def show_balance(self):

      return f"💸Your balance is:{self.__balance} €"

account = BankAccount(2000)
print(account.deposit(5000))
print(account.withdraw(700))
print(account.show_balance())

