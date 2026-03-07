# ТЕМА: Custom Exceptions — своя иерархия ошибок


class BankError(Exception):
    pass


class InsufficientFundsError(BankError):
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance {balance}, attempted withdrawal {amount}")


class AccountLockedError(BankError):
    def __init__(self, account_id: str):
        super().__init__(f"Account {account_id} is locked")


def withdraw(balance: float, amount: float, locked: bool = False) -> float:
    if locked:
        raise AccountLockedError("ACC-001")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    print(withdraw(100.0, 200.0))
except InsufficientFundsError as e:
    print(f"Error: {e}")

try:
    print(withdraw(100.0, 50.0, locked=True))
except AccountLockedError as e:
    print(f"Error: {e}")

print(withdraw(100.0, 50.0))
