from pydantic import BaseModel, field_validator
from typing import Optional


class User(BaseModel):
    name: str
    email: str
    age: int

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Age must be positive")
        return v


class Transaction(BaseModel):
    amount: float
    currency: str = "USD"
    user_id: int
    description: Optional[str] = None

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v


user = User(name="Denis", email="denis@test.com", age=22)
print(user)

tx = Transaction(amount=100.0, user_id=1, description="test payment")
print(tx)

try:
    bad_user = User(name="Bad", email="bad@test.com", age=-5)
except Exception as e:
    print(f"Validation error: {e}")

try:
    bad_tx = Transaction(amount=-50.0, user_id=1)
except Exception as e:
    print(f"Validation error: {e}")
