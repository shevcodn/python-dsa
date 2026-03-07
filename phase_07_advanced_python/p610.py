import pytest
import asyncio
from unittest.mock import Mock, patch, mock_open

class PaymentService:
    def __init__(self, gateway):
        self.gateway = gateway
        self.transactions = []


    def process(self, amount, currency="USD"):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        result = self.gateway.charge(amount, currency)
        self.transactions.append(result)
        return result
    
    async def process_async(self, amount):
        await asyncio.sleep(0.01)
        return self.process(amount)
    
    def save_report(self, path):
        with open(path, "w") as f:
            f.write(f"Transactions: {len(self.transactions)}")

@pytest.mark.asyncio
async def test_process_success():
    gateway = Mock()
    gateway.charge.return_value = {"status": "success"}
    service = PaymentService(gateway)
    result = await service.process_async(100)
    assert result["status"] == "success"
    assert len(service.transactions) == 1

@pytest.mark.asyncio
async def test_process_invalid():
    gateway = Mock()
    service = PaymentService(gateway)
    with pytest.raises(ValueError):
        await service.process_async(-50)

@pytest.mark.asyncio
async def test_process_multiple():
    gateway = Mock()
    gateway.charge.side_effect = [{"status": "success"}, {"status": "failed"}]
    service = PaymentService(gateway)
    result1 = await service.process_async(100)
    result2 = await service.process_async(200)
    assert result1["status"] == "success"
    assert result2["status"] == "failed"
    assert len(service.transactions) == 2

@pytest.mark.asyncio
async def test_process_async():
    gateway = Mock()
    gateway.charge.return_value = {"status": "success"}
    service = PaymentService(gateway)
    result = await service.process_async(150)
    assert result["status"] == "success"
    assert len(service.transactions) == 1

@pytest.mark.asyncio
async def test_save_report():
    gateway = Mock()
    gateway.charge.return_value = {"status": "success"}
    service = PaymentService(gateway)
    await service.process_async(100)
    m = mock_open()
    with patch("builtins.open", m):
        service.save_report("report.txt")
        m.assert_called_with("report.txt", "w")
        handle = m()
        handle.write.assert_called_with("Transactions: 1")

@pytest.fixture
def payment_service():
    gateway = Mock()
    gateway.charge.return_value = {"status": "success"}
    return PaymentService(gateway)