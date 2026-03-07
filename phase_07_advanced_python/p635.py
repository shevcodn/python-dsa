from dataclasses import dataclass, field
from typing import Optional, List, Protocol, TypedDict, Literal

class AccountConfig(TypedDict):
    owner: str
    currency: Literal["USD", "EUR", "GBP"]
    limit: float

class PaymentProcessor(Protocol):
    def process(self, amount: float) -> bool: ...

@dataclass
class Account:
    config: AccountConfig
    balance: float = 0.0
    history: List[str] = field(default_factory=list)

    def deposit(self, amount: float, processor: Optional[PaymentProcessor] = None) -> bool:
        if processor:
            if not processor.process(amount):
                self.history.append(f"Failed deposit of {amount} {self.config['currency']}")
                return False
        self.balance += amount
        self.history.append(f"Deposited {amount} {self.config['currency']}")
        return True
    
    def withdraw(self, amount: float, processor: Optional[PaymentProcessor] = None) -> bool:
        if amount > self.balance:
            self.history.append(f"Failed withdrawal of {amount} {self.config['currency']}")
            return False
        if processor:
            if not processor.process(amount):
                self.history.append(f"Failed withdrawal of {amount} {self.config['currency']}")
                return False
        self.balance -= amount
        self.history.append(f"Withdrew {amount} {self.config['currency']}")
        return True 
    
    def get_history(self) -> List[str]:
        return self.history
    
class StripeProcessor:
    def process(self, amount: float) -> bool:
        print(f"Processing payment of {amount} through Stripe")
        return True
    
def pay(processor: PaymentProcessor, amount: float) -> bool:
    return processor.process(amount)
    
account = Account(config={"owner": "Denis", "currency": "USD", "limit": 10000.0})
stripe = StripeProcessor()
account.deposit(500.0, processor=stripe)
account.withdraw(200.0, processor=stripe)
print(f"Balance: {account.balance} {account.config['currency']}")
print("Transaction History:")
for entry in account.get_history():
    print(entry)

