import pytest

class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")
        
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount


def test_withdraw_raises():
    wallet = Wallet(100)
    with pytest.raises(InsufficientFundsError) as exc:
        wallet.withdraw(150)
    assert exc.value.amount == 150
    assert exc.value.balance == 100

def test_withdraw_message():
    wallet = Wallet(50)
    with pytest.raises(InsufficientFundsError, match=r"Cannot withdraw 100, balance is 50") as exc_info:
        wallet.withdraw(100)
    assert exc_info.value.amount == 100
    assert exc_info.value.balance == 50

def test_withdraw_ok():
    wallet = Wallet(200)
    wallet.withdraw(50)
    assert wallet.balance == 150