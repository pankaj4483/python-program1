class Bankaccount:
    def __init__(self):
        self.__balance=0

    def deposite(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

account=Bankaccount()
account.deposite(1000)
account.withdraw(2000)
print(account.get_balance())
account.withdraw(1000)

