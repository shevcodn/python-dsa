from pydantic import BaseModel, field_validator
from typing import Optional

class PaymentRequest(BaseModel):
    amount: float
    currency: str = "USD"
    user_id: int

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v
    

class PaymentResult(BaseModel):
    success: bool
    transaction_id: Optional[str] = None
    message: Optional[str] = None

    
class PaymentService:
    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        if request.amount > 1000:
            return PaymentResult(success=False, message="Amount exceeds limit")
        return PaymentResult(success=True, transaction_id="tx12345", message="OK")
    
service = PaymentService()
request = PaymentRequest(amount=500.0, user_id=1)
result = service.process_payment(request)
print(result)

try:
    bad_request = PaymentRequest(amount=-50.0, user_id=1)
except Exception as e:
    print(f"Validation error: {e}")
    

    