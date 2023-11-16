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
    ## accessor tests needed:
    # 1. account_type accessor - returns account type attribute value (DEMONSTRATED)
    # 2. account_number accessor - returns account number attribute value
    # 3. balance accessor - returns balance attribute value
    def test_account_type_accessor(self):
        # Arrange and Act
        account = Account(AccountType.SAVINGS, 999999, 100.00)
        # Assert
        self.assertEqual(account.account_type, AccountType.SAVINGS)
    
    ## __init__ tests needed:
    # 1. valid inputs  (DEMONSTRATED)
    # 2. invalid account type (DEMONSTRATED)
    # 3. invalid account number (non-numeric)
    # 4. invalid account number (negative)
    # 4. invalid balance (non-numeric)
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

    ## mutator tests needed:
    # 1. account_type mutator - valid input (DEMONSTRATED)
    # 2. account_type mutator - invalid input (DEMONSTRATED)
    # 3. account_number mutator - valid input
    # 4. account_number mutator - non-numeric
    # 5. account_number mutator - negative
    # 6. balance mutator - valid input
    # 7. balance mutator - non-numeric
    def test_account_type_mutator_valid(self):
        # Arrange
        account = Account(AccountType.MORTGAGE, 100, 100)
        expected = AccountType.CHEQUING
        # Act
        account.account_type = AccountType.CHEQUING
        # Assert
        self.assertEqual(expected, account.account_type)
    def test_account_type_mutator_invalid(self):
        # Arrange
        account = Account(AccountType.MORTGAGE, 100, 100)
        expected = "Invalid account type."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            account.account_type = "INVALID"
        # Assert
        self.assertEqual(expected, str(context.exception))
    ## __repr__ tests:
    #1. ensure expected representation is returned. (DEMONSTRATED)
    def test_repr_correct(self):
        # Arrange
        account = Account(AccountType.MORTGAGE, 1234567, -493912.53)
        expected = "AccountType.MORTGAGE | 1234567 | -493912.53"
        # Act
        actual = repr(account)
        # Assert
        self.assertEqual(expected, actual)
    ## __str__ tests:
    # 1. ensure expected string representation is returned. (DEMONSTRATED)
    def test_str_correct(self):
        # Arrange
        account = Account(AccountType.MORTGAGE, 1234567, -493912.53)
        expected = (f"Type: Mortgage"
                    + f"\nAccount Number: 1234567"
                    + f"\nBalance: $-493,912.53")
        # Act
        actual = str(account)
        # Assert
        self.assertEqual(expected , actual)
    ## update_balance tests:
    #1. valid deposit
    #2. valid withdraw
    #3. non-numeric amount
    #4. insufficient funds  (DEMONSTRATED)
    def test_update_balance_insufficient_funds(self):
        # Arrange
        account = Account(AccountType.SAVINGS, 1234567, 5000)
        expected = "Insufficient Funds!"
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            account.update_balance(-5001)
        self.assertEqual(expected, str(context.exception))
