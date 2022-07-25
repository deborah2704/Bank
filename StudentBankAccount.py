from BankAccount import BankAccount
from PersonalInfo import PersonalInfo

class StudentBankAccount(BankAccount):
    def __init__(self, personal_info: PersonalInfo, balance, college) -> None:
        super().__init__(personal_info, balance)
        self.college = college

    def __str__(self) -> str:
        return super().__str__() + f'\nCollege: {self.college}'

    def withdraw(self, amount: int):
        """
            amount: int
        """
        if self.balance - amount >= 0:
            super().withdraw(amount)