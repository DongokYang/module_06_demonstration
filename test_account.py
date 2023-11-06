"""
Description: Module 06 demonstration -
    Unit Tests: Unit tests for the BankAccount class.
Author: Nithya John
Date: 2023-11-06
Usage: to execute tests:
    python -m unittest -v tests/account_tests.py
"""
import unittest
from account.account import Account
from account.account_type import AccountType
class AccountTests(unittest.TestCase):
    def test_account_type_accessor(self):
        # Arrange and Act
        account = Account(AccountType.SAVINGS, 999999, 100.00)
        # Assert
        self.assertEqual(account.account_type, AccountType.SAVINGS)

    ## accessor tests needed:
    # 1. account_type accessor - returns account type attribute value (DEMONSTRATED)
    # 2. account_number accessor - returns account number attribute value
    # 3. balance accessor - returns balance attribute value
    def test_init_valid(self):
        # Arrange
        account_type = AccountType.MORTGAGE
        account_number = 123456789
        balance = 100
        # Act
        bank_account = Account(account_type, account_number,balance)
        # Assert:
        self.assertEqual(bank_account._account_type, account_type)
        self.assertEqual(bank_account._account_number, account_number)
        self.assertEqual(bank_account._balance, balance)
    def test_init_invalid_account_type(self):
        # Arrange
        account_type = "INVALID"
        account_number = 123456789
        balance = 100
        expected = "Invalid account type."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            Account(account_type, account_number, balance)
        self.assertEqual(expected, str(context.exception))
        
    ## __init__ tests needed:
    # 1. valid inputs  (DEMONSTRATED)
    # 2. invalid account type (DEMONSTRATED)
    # 3. invalid account number (non-numeric)
    # 4. invalid account number (negative)
    # 4. invalid balance (non-numeric)


    ## mutator tests needed:
    # 1. account_type mutator - valid input (DEMONSTRATED)
    # 2. account_type mutator - invalid input (DEMONSTRATED)
    # 3. account_number mutator - valid input
    # 4. account_number mutator - non-numeric
    # 5. account_number mutator - negative
    # 6. balance mutator - valid input
    # 7. balance mutator - non-numeric

    ## __repr__ tests:
    #1. ensure expected representation is returned. (DEMONSTRATED)

    ## __str__ tests:
    # 1. ensure expected string representation is returned. (DEMONSTRATED)

    ## update_balance tests:
    #1. valid deposit
    #2. valid withdraw
    #3. non-numeric amount
    #4. insufficient funds  (DEMONSTRATED)
