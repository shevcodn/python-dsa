from pydantic import BaseModel, field_validator
from typing import Optional


class Account(BaseModel):
    id: int
    owner: str
    balance: float

    @field_validator("balance")
    @classmethod
    def balance_must_be_non_negative(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Balance must be non-negative")
        return v

class TransferRequest(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v
    
class AccountNotFoundError(Exception):
    def __init__(self, account_id: int):
        super().__init__(f"Account with id {account_id} not found")
        self.account_id = account_id

class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float):
        super().__init__(f"Need {amount}, have {balance}")
        self.balance = balance
        self.amount = amount

try:
    account = Account(id=1, owner="Denis", balance=-100.0)
except Exception as e:
    print(f"Validation error: {e}")
    if isinstance(e, AccountNotFoundError):
        print(f"Account not found: {e.account_id}")
    elif isinstance(e, InsufficientFundsError):
        print(f"Insufficient funds: need {e.amount}, have {e.balance}")

class TransferService:

    def __init__(self):
        self.accounts: dict[int, Account] = {}

    def add_account(self, account: Account) -> None:
        self.accounts[account.id] = account

    def transfer(self, request: TransferRequest) -> bool:
        from_account = self.accounts.get(request.from_account_id)
        to_account = self.accounts.get(request.to_account_id)

        if from_account is None:
            raise AccountNotFoundError(request.from_account_id)
        if to_account is None:
            raise AccountNotFoundError(request.to_account_id)
        if from_account.balance < request.amount:
            raise InsufficientFundsError(from_account.balance, request.amount)
        
        from_account.balance -= request.amount
        to_account.balance += request.amount
        return True
    
service = TransferService()
service.add_account(Account(id=1, owner="Denis", balance=1000.0))
service.add_account(Account(id=2, owner="Pavel", balance=500.0))
request = TransferRequest(from_account_id=1, to_account_id=2, amount=200.0)
try:
    result = service.transfer(request)
    print(f"Transfer successful: {result}")
except Exception as e:
    print(f"Transfer failed: {e}")
    if isinstance(e, AccountNotFoundError):
        print(f"Account not found: {e.account_id}")
    elif isinstance(e, InsufficientFundsError):
        print(f"Insufficient funds: need {e.amount}, have {e.balance}")