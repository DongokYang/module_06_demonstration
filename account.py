"""
Description: Module 06 demonstration -
    Class: A class that maintains bank accounts 
    at PiXELL River.
Author: Nithya John
Date: 2023-11-06
Usage: To incorporate this class into a class or 
program, import this using:
from account.account_type import Account 
"""
from account.account_type import AccountType

class Account:
    """
    A class that maintains bank account data.

    Attributes:
        _account_type (AccountType): The type of bank account.
        _account_number (int): Account number of the bank account.
        _balance (float): Balance of the bank account.

    Methods (instance methods):
        update_balance(): Modifies the balance of the bank account.
    """

## __INIT__
    def __init__(self, account_type: AccountType, 
                account_number: int, balance: float):
        """
        Initialize a new account object with an account type,
        account number and balance.
        Args:
            account_type(AccountType): The account type for the account.
            account_number(int): The account number for the account.
            balance (float): The balance of the account.
        Returns:
            None
        Raises:
            ValueError: When the account type is invalid.
            ValueError: When the account number is non-numeric.
            ValueError: When the account number is negative.
            ValueError: When the balance is non-numeric.
        """
        if isinstance(account_type, AccountType):
            self._account_type = account_type
        else:
            raise ValueError("Invalid account type.")
        
        try:
            account_number = int(account_number)
        except ValueError:
            raise ValueError("Account number must be a whole number.")
        
        if account_number < 0:
            raise ValueError("Account number must be positive.")

        try:
            balance = float(balance)
        except ValueError:
            raise ValueError("Balance must be numeric.")
        
        self._account_number = account_number
        self._balance = balance

## ACCESSORS
    @property
    def account_type(self) ->AccountType:
        """
        Accessor for _account_type attribute.
        """
        return self._account_type

    @property
    def account_number(self) ->int:
        """
        Accessor for _account_number attribute.
        """
        return self._account_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for _balance attribute.
        """
        return self._balance
    

## MUTATORS
    @account_type.setter
    def account_type(self, value: AccountType):
        """
        Sets the account type of the Account.
        Args:
            value (AccountType): The type of account.
        Raises:
            ValueError: When the value provided is 
            not a valid AccountType.
        """
        if isinstance(value, AccountType):
            self._account_type = value
        else:
            raise ValueError("Invalid account type.")
        
    @account_number.setter
    def account_number(self, value: int):
        """
        Sets the account number of the Account.
        Args:
            value (int): The account number.
        Raises:
            ValueError: When the value provided not numeric.
            ValueError: When the value provided is negative.
        """
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Account number must be numeric.")
        
        if value < 0:
            raise ValueError("Account number must be positive.")
        
        self._account_number = value


    @balance.setter
    def balance(self, value: float):
        """
        Sets the balance of the Account.
        Args:
            value (float): The account balance.
        Raises:
            ValueError: When the value provided not numeric.
        """
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Balance must be numeric.")
        
        self._balance = value
    ## __REPR__
    # given docstring for __repr__
    def __repr__(self):
        """
        Provides a representation of an Account object.
        Returns:
            str: A representation of a bank account.
                format: account_type | account_number | balance
                example: [AccountType.MORTGAGE | 1234567 | -493912.53]
        """
        return (f"{self.account_type} | "
                + f"{self.account_number} | "
                + f"{self.balance}")

## __STR__
    # given docstring for __str__
    def __str__(self):
        """
        Returns a string representation of the class.
        Returns:
            str:  A string representation of a bank account.
                format:  Type: AccountType
                        Account Number: account number
                        Balance: $balance
                example:
                        Type: Mortgage
                        Account Number: 1234567
                        Balance: $-493,912.53    
        """
        return (f"Type: {self.account_type.name.title()}"
                + f"\nAccount Number: {self.account_number}"
                + f"\nBalance: ${self.balance:,.2f}")

## UPDATE_BALANCE
# given docstring for update_balance()
    def update_balance(self, amount:float)->None:
        """
        Update the balance of the account.  All deposits (+) are 
        permitted.  Withdraws (-) are only permitted if sufficient funds.

        Args:
            amount(float): amount of transaction.  Positive values 
            are deposited, negative values are withdrawn.

        Returns:
            None
        Raises:
            ValueError: When the amount is non-numeric.
            ValueError: When there are insufficient funds.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Amount must be numeric.")
        
        if amount > 0:
            self.balance += amount
        elif amount < 0 and abs(amount) <= self.balance:
            self.balance += amount
        else:
            raise ValueError("Insufficient Funds!")
