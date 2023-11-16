"""
Description: Module 06 demonstration -
    Enumerations: An enumeration of the types 
    of bank accounts that PiXELL River supports.
Author: Nithya John
Date: 2023-11-06
Usage: To incorporate this enumeration into a class or 
program, import this enum using:
from account.account_type import AccountType 
"""

from enum import Enum
class AccountType(Enum):
    """
    An enumeration of the types of bank accounts supported
    by PiXELL River Financial.
    Values:
        SAVINGS: a savings account
        CHEQUING: a chequing account
        MORTGAGE: a mortgage account
        CREDIT: a credit account
    """
    SAVINGS = 1
    CHEQUING = 2
    MORTGAGE = 3
    CREDIT = 4

# # Using the enumeration
# account = AccountType.MORTGAGE
# print(account)
# print(account.value)

# # Compare names and values using ==
# print(AccountType.MORTGAGE == AccountType.CREDIT)
# print(AccountType.MORTGAGE.value == AccountType.CREDIT.value)

# # Membership checking using 'in'
# print(AccountType.MORTGAGE in AccountType)
# # print(AccountType.INVESTMENT in AccountType)

# # Membership checking with 'isinstance()' function
# print(isinstance(AccountType.MORTGAGE,AccountType))
# # print(isinstance(AccountType.INVESTMENT,AccountType))