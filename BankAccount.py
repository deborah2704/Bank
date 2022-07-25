from PersonalInfo import PersonalInfo

class BankAccount:
    def __init__(self, personal_info: PersonalInfo, balance: int) -> None:
        self.personal_info = personal_info
        self.balance = balance

    def __str__(self) -> str:
        return f'{self.personal_info.__str__()}\nBalance: {self.balance}'

    def withdraw(self, amount: int):
        """
            amount: int
        """
        self.balance = self.balance - amount

    def deposit(self, amount: int):
        """
            amount: int
        """
        self.balance = self.balance + amount