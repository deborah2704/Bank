from re import I
from statistics import median
import numpy as np
import xml.etree.ElementTree
import sys
from BankAccount import BankAccount
from BusinessBankAccount import BusinessBankAccount
from PersonalInfo import PersonalInfo
from StudentBankAccount import StudentBankAccount

class Bank:
    def __init__(self) -> None:
        self.accounts = {}

    def load_and_parse_init_data(self, file: str):
        """
            file: str
        """
        tree = xml.etree.ElementTree.parse(file)
        for child in tree.getroot():
            type_account = child.get('type')
            pi_elt = child.find('personalInfo')
            name = pi_elt.find('name').text
            id = pi_elt.find('id').text
            phone = pi_elt.find('phone').text
            email = pi_elt.find('email').text
            personal_info = PersonalInfo(name, id, phone, email)
            if type_account == 'BankAccount':
                account = BankAccount(personal_info, 0)
                self.add_new_account(id, account)
            if type_account == 'StudentBankAccount':
                college = child.find('college').text
                account = StudentBankAccount(personal_info, 0, college)
                self.add_new_account(id, account)
            if type_account == 'BusinessBankAccount':
                business = child.find('business').text
                account = BusinessBankAccount(personal_info, 0, business)
                self.add_new_account(id, account)

    def add_new_account(self, id: str, account: BankAccount|StudentBankAccount|BusinessBankAccount):
        """
            id: str
            account: BankAccount|StudentBankAccount|BusinessBankAccount
        """
        self.accounts[id] = account

    def delete_by_userid(self, id: str):
        """
            id: str
        """
        del self.accounts[id]

    def withdraw_by_userid(self, id: str, amount: int):
        """
            id: str
            amount: int
        """
        self.accounts[id].withdraw(amount)

    def deposit_by_userid(self, id: str, amount: int):
        """
            id: str
            amount: int
        """
        self.accounts[id].deposit(amount)

    def calc_balance_statistics(self):
        total = 0
        balance_list = []
        for account in self.accounts.values():
            total += account.balance
            balance_list.append(account.balance)
        avg = total / len(self.accounts)
        med = median(balance_list)
        perc90 = np.percentile(balance_list, 90)
        perc10 = np.percentile(balance_list, 10)
        return {'average': avg, 'median': med, '90th percentile': perc90, '10th percentile': perc10}

    def __str__(self) -> str:
        accounts_str = '\n---------------------------------\n'
        for k, v in self.accounts.items():
            accounts_str += v.__str__()
            accounts_str += '\n---------------------------------\n'
        return accounts_str


def main():
    if (sys.argv[1]):
        file = sys.argv[1]
        b = Bank()
        b.load_and_parse_init_data(file)
        print(b.__str__())
        b.deposit_by_userid('1234567', 150000)
        print(b.__str__())
        b.withdraw_by_userid('1234567', 1000)
        print(b.__str__())
        print(b.calc_balance_statistics())
        b.delete_by_userid('1234567')
        print(b.__str__())


if __name__ == "__main__":
    main()

