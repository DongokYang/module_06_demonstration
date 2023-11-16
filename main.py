"""
Description: Module 06 demonstration -
    Client Program: A program that makes use of the Account class
    and the AccountType enumeration.
Author: Nithya John
Date: 2023-11-10
Usage: To run: Press the play button in the top left 
corner of VS code. or in the terminal type:
python main.py
"""
# UNCOMMENT FOR DEMO:
from account.account import Account
from account.account_type import AccountType

def main():
    
    # execute constructor (__init__)
    chequing_account = Account(AccountType.CHEQUING, 123213, 599.35)
    credit_account = Account(AccountType.CREDIT, 59382, -859.33)

    # execute __repr__
    print(repr(chequing_account))
    print(repr(credit_account))
    print()

    # use mutator to change balance (note method brackets are not used
    # because @balance.setter decorator was used when defined.)
    try:
        chequing_account.balance = 699.43
    except ValueError as e:
        print(e)



    # use accessor to print account number (note method brackets are 
    # note used because @property decorator was used when defined.)
    print(credit_account.account_number)

    # using mutator with invalid account number:
    try:
        chequing_account.account_number = -55
    except ValueError as e:
        print(e)

    # use update balance with valid amount
    try:
        chequing_account.update_balance(4.95)
    except ValueError as e:
        print(e)

    print()
    # use update balance with invalid amount
    try:
        chequing_account.update_balance(-5000)
    except ValueError as e:
        print(e)

    print()
    # use __str__
    print(chequing_account)

if __name__ == "__main__":
    main()

 
