import logging
from pydantic import BaseModel, field_validator
from typing import Optional

exception_logger = logging.getLogger("exceptions")
exception_logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s")
handler.setFormatter(formatter)
exception_logger.addHandler(handler)

class Account(BaseModel):
    id: int
    owner: str
    balance: float
    daily_limit: float = 5000.0
    daily_spent: float = 0.0

    @field_validator("balance")
    @classmethod
    def balance_must_be_non_negative(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Balance must be non-negative")
        return v
    
class TransferRequest(BaseModel):
    from_id: int
    to_id: int
    amount: float

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v
    
class TransferResult(BaseModel):
    success: bool
    from_owner: Optional[str] = None
    to_owner: Optional[str] = None
    amount: Optional[float] = None
    message: Optional[str] = None

class TransactionContext:
    def __init__(self, description: str):
        self.description = description

    def __enter__(self):
        logging.info(f"Starting transaction: {self.description}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            exception_logger.error(f"Transaction failed: {self.description} - {exc_val}")
        else:
            logging.info(f"Transaction succeeded: {self.description}")

class BankingService(BaseModel):
    accounts: dict

    def add_account(self, account: Account) -> None:
        self.accounts[account.id] = account

    def get_account(self, id: int) -> Optional[Account]:
        return self.accounts.get(id)
    
    def transfer(self, request: TransferRequest) -> TransferResult:
        with TransactionContext(f"Transfer {request.amount} from {request.from_id} to {request.to_id}"):
            from_account = self.get_account(request.from_id)
            to_account = self.get_account(request.to_id)

            if from_account is None:
                return TransferResult(success=False, message=f"From account {request.from_id} not found")
            if to_account is None:
                return TransferResult(success=False, message=f"To account {request.to_id} not found")
            if request.amount > from_account.balance:
                return TransferResult(success=False, message="Insufficient funds")
            if from_account.daily_spent + request.amount > from_account.daily_limit:
                return TransferResult(success=False, message="Daily limit exceeded")
            
            from_account.balance -= request.amount
            from_account.daily_spent += request.amount
            to_account.balance += request.amount
            
            return TransferResult(success=True, from_owner=from_account.owner, to_owner=to_account.owner, amount=request.amount, message="Transfer successful")
        
service = BankingService(accounts={})
service.add_account(Account(id=1, owner="Denis", balance=1000.0))
service.add_account(Account(id=2, owner="Pavel", balance=500.0))
request = TransferRequest(from_id=1, to_id=2, amount=200.0)
result = service.transfer(request)
print(result)


