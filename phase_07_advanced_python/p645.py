import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

TRANSACTION_WITHDRAW = "withdraw"
TRANSACTION_DEPOSIT = "deposit"


class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float):
        super().__init__(f"Need {amount}, have {balance}")


class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        self.history: list = []

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            return False
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        logger.info(f"Withdrew {amount} from {self.owner}'s account. New balance: {self.balance}")
        self.history.append((TRANSACTION_WITHDRAW, amount))
        return True

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self.balance += amount
        logger.info(f"Deposited {amount} to {self.owner}'s account. New balance: {self.balance}")
        self.history.append((TRANSACTION_DEPOSIT, amount))
        return True

    def get_history(self) -> list:
        return self.history


account = BankAccount("Denis", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print(account.balance)
print(account.get_history())

try:
    account.withdraw(5000.0)
except InsufficientFundsError as e:
    print(f"Error: {e}")
