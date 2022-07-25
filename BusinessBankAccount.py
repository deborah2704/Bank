from BankAccount import BankAccount
from PersonalInfo import PersonalInfo

class BusinessBankAccount(BankAccount):
    def __init__(self, personal_info: PersonalInfo, balance, business) -> None:
        super().__init__(personal_info, balance)
        self.business = business
        self.commission = 1.50/100

    def __str__(self) -> str:
        return super().__str__() + f'\nBusiness: {self.business}'

    def withdraw(self, amount: int):
        """
            amount: int
        """
        super().withdraw(amount)
        self.balance = self.balance - (amount * self.commission)

    def deposit(self, amount: int):
        """
            amount: int
        """
        super().deposit(amount)
        self.balance = self.balance - (amount * self.commission)
