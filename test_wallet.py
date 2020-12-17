"""
Test harness for the Wallet class
"""
import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture(name='empty_wallet')
def fixture_empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture(name='wallet')
def fixture_wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    '''Test setting the wallet's default zero balance'''
    assert empty_wallet.balance == 0

def test_setting_initial_amount():
    '''Test setting the wallet's initial balance of 100'''
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash(wallet):
    '''Test adding cash to the wallet'''
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    '''Test spending cash from the wallet'''
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(wallet):
    '''Test spending more cash than the wallet contains'''
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)

@pytest.fixture(name='my_wallet')
def fixture_my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_tramsactions(my_wallet, earned, spent, expected):
    '''Test wallet transactions'''
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
