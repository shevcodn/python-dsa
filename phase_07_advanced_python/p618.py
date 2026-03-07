import pytest
from unittest.mock import Mock

class Transaction:
    def __init__(self, amount, currency="USD"):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.amount = amount
        self.currency = currency
        self.status = "pending"

    def approve(self):
        self.status = "approved"

    def reject(self, reason):
        self.status = "rejected"
        self.reason = reason

class TransactionService:
    def __init__(self, db, notifier):
        self.db = db
        self.notifier = notifier

    def process(self, amount, currency="USD"):
        tx = Transaction(amount, currency)
        tx.approve()
        self.db.save(tx)
        self.notifier.notify(f"Transaction approved: {tx.amount} {tx.currency}")
        return tx
    
@pytest.fixture
def service():
    return TransactionService(Mock(), Mock())

def test_process_success(service):
    tx = service.process(100)
    assert tx.status == "approved"
    assert tx.amount == 100
    service.db.save.assert_called_once()

def test_process_invalid(service):
    with pytest.raises(ValueError):
        service.process(-50)

def test_notify_called(service):
    service.process(200, "CAD")
    service.notifier.notify.assert_called_once_with("Transaction approved: 200 CAD")

def test_reject():
    tx = Transaction(100)
    tx.reject("fraud detected")
    assert tx.status == "rejected"
    assert tx.reason == "fraud detected"
