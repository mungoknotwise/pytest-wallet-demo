"""
The Wallet
"""
class InsufficientAmount(Exception):
    """
    A class to represent an insufficent amount of money to spend
    """
    # pass

class Wallet():
    """
    A class to represent a wallet containing money.

    ...

    Attributes
    ----------
    balance : int
        amount of money currently in the wallet
    """
    def __init__(self, initial_amount = 0):
        """
        Constructs the necessary attributes for the wallet object.

        Parameters
        ----------
            initial_amount : int
                starting amount of money in the wallet
        """
        self.balance = initial_amount

    def spend_cash(self, amount):
        '''Takes in an amount and deducts the amount from the wallet balance'''
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        '''Takes in an amount and adds the amount to the wallet balance'''
        self.balance += amount
