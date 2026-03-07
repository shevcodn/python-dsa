from typing import TypedDict

class Position(TypedDict):
    ticker: str
    shares: int
    avg_price: float

class Transaction(TypedDict):
    id: int
    amount: float
    currency: str
    status: str

def get_value(position: Position) -> float:
    return position["shares"] * position["avg_price"]

def is_complete(transaction: Transaction) -> bool:
    return transaction["status"] == "complete"

position = Position(ticker="AAPL", shares=10, avg_price=250.0)
transactions = [Transaction(id=1, amount=2500.0, currency="USD", status="complete")]
if complete := is_complete(transactions[0]):
    print(f"Transaction {transactions[0]['id']} is complete.")