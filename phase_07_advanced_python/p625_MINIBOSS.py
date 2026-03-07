import pytest
from unittest.mock import Mock

class Wallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

class WalletService:
    def __init__(self, db, notifier):
        self.db = db
        self.notifier = notifier

    def create(self, owner):
        wallet = Wallet(owner)
        self.db.save(wallet)
        return wallet

    def transfer(self, sender, receiver, amount):
        sender.withdraw(amount)
        receiver.deposit(amount)
        self.notifier.notify(f"Transfer {amount} from {sender.owner} to {receiver.owner}")


@pytest.fixture
def service():
    return WalletService(db=Mock(), notifier=Mock())

@pytest.fixture
def sender():
    return Wallet("Denis", balance=500)

@pytest.fixture
def receiver():
    return Wallet("Pavel", balance=100)

def test_create(service):
    wallet = service.create("Denis")
    assert wallet.owner == "Denis"
    service.db.save.assert_called_once()

def test_transfer_success(service, sender, receiver):
    service.transfer(sender, receiver, 200)
    assert sender.balance == 300
    assert receiver.balance == 300
    service.notifier.notify.assert_called_once_with("Transfer 200 from Denis to Pavel")

def test_transfer_insufficient(service, sender, receiver):
    with pytest.raises(ValueError) as exc:
        service.transfer(sender, receiver, 1000)
    assert str(exc.value) == "Insufficient funds"

@pytest.mark.parametrize("amount, expected", [
    (10, 10),
    (50, 50),
    (100, 100)
])
def test_deposit(amount, expected):
    wallet = Wallet("test", balance=0)
    wallet.deposit(amount)
    assert wallet.balance == expected