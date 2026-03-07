from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Trade:
    ticker: str
    shares: int
    price: float
    side: str # "buy" or "sell"

    def total(self) -> float:
        return self.shares * self.price
    
@dataclass
class Portfolio:
    owner: str
    trades: List[Trade] = field(default_factory=list)

    def add_trade(self, trade: Trade) -> None:
        self.trades.append(trade)
        print(f"Added trade: {trade.side} {trade.shares} shares of {trade.ticker} at ${trade.price}")

    def total_invested(self) -> float:
        return sum(trade.total() for trade in self.trades if trade.side == "buy")

owned_portfolio = Portfolio(owner="Denis")
owned_portfolio.add_trade(Trade(ticker="AAPL", shares=10, price=150.0, side="buy"))
owned_portfolio.add_trade(Trade(ticker="TSLA", shares=5, price=300.0, side="buy"))
owned_portfolio.add_trade(Trade(ticker="AAPL", shares=5, price=155.0, side="sell"))
print(f"Total invested: ${owned_portfolio.total_invested():.2f}")
