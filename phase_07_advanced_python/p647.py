from pydantic import BaseModel, field_validator
from typing import Optional


class Address(BaseModel):
    street: str
    city: str
    country: str ="CA"

class BankUser(BaseModel):
    id: int
    name: str
    address: Address

class Transfer(BaseModel):
    sender: BankUser
    receiver: BankUser
    amount: float
    validate: bool = True

    def execute(self) -> bool:
        if self.validate:
            if self.amount <= 0:
                raise ValueError("Amount must be positive")
            if self.sender.address.country != self.receiver.address.country:
                raise ValueError("Cross-border transfers are not allowed")
        return True
    
sender = BankUser(id=1, name="Denis", address=Address(street="Main St", city="Toronto", country="CA"))
receiver = BankUser(id=2, name="Pavel", address=Address(street="Second St", city="Vancouver", country="CA"))
transfer = Transfer(sender=sender, receiver=receiver, amount=100.0)
print(transfer.execute())

