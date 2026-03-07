import pytest
from unittest.mock import Mock

class PaymentGateway:
    def charge(self, amount, card):
        raise NotImplementedError()
    
class OrderService:
    def __init__(self, gateway, inventory):
        self.gateway = gateway
        self.inventory = inventory
        self.orders = []

    def place_order(self, item, amount, card):
        if not self.inventory.has_stock(item):
            raise ValueError("Item out of stock")
        result = self.gateway.charge(amount, card)
        if result["status"] == "ok":
            self.inventory.reduce(item)
            self.orders.append({"item": item, "amount": amount})
            return {"success": True, "order_id": len(self.orders)}
        return {"success": False}
    
@pytest.fixture
def gateway():
    m = Mock()
    m.charge.return_value = {"status": "ok"}
    return m

@pytest.fixture
def inventory():
    m = Mock()
    m.has_stock.return_value = True
    return m

@pytest.fixture
def order_service(gateway, inventory):
    return OrderService(gateway, inventory)

def test_full_order_flow(order_service, gateway, inventory):
    result = order_service.place_order("AAPL", 250, "card_123")
    assert result["success"] is True
    assert result["order_id"] == 1
    gateway.charge.assert_called_once_with(250, "card_123")
    inventory.reduce.assert_called_once_with("AAPL")

def test_no_stock(order_service, inventory):
    inventory.has_stock.return_value = False
    with pytest.raises(ValueError, match="Item out of stock"):
        order_service.place_order("TSLA", 400, "card_123")

def test_payment_failed(order_service, gateway):
    gateway.charge.return_value = {"status": "failed"}
    result = order_service.place_order("NVDA", 180, "card_123")
    assert result["success"] is False
    assert len(order_service.orders) == 0