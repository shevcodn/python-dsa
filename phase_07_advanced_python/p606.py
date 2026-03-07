from unittest.mock import Mock

def process_payment(gateway, amount):
    result = gateway.charge(amount)
    if result["status"] == "success":
        return True
    return False

def test_payment_success():
    gateway = Mock()
    gateway.charge.return_value = {"status": "success"}
    assert process_payment(gateway, 100)

def test_payment_failed():
    gateway = Mock()
    gateway.charge.return_value = {"status": "failed"}
    assert not process_payment(gateway, 100)

def test_payment_called_with():
    gateway = Mock()
    gateway.charge.return_value = {"status": "success"}
    process_payment(gateway, 250)
    gateway.charge.assert_called_with(250)

