from typing import List, Dict, Tuple, Set

def get_names(users: List[str]) -> List[str]:
    return [u.upper() for u in users]

def get_prices(portfolio: Dict[str, float]) -> Dict[str, float]:
    return {k: v * 1.1 for k, v in portfolio.items()}

def get_range(start: int, end: int) -> Tuple[int, int]:
    return (start, end)

def unique_tickers(tickers: Set[str]) -> Set[str]:
    return set(t.upper() for t in tickers)

print(get_names(["Alice", "Bob", "Charlie"]))
print(get_prices({"AAPL": 150.0, "TSLA": 300.0}))
print(get_range(1, 10))
print(unique_tickers({"aapl", "tsla", "nvda"}))