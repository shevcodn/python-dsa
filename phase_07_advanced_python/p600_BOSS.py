import asyncio
import httpx
from rich.console import Console
from rich.table import Table

class FintechAggregator:
    def __init__(self, max_concurrent=3):
        self.cache = {}
        self.sem = asyncio.Semaphore(max_concurrent)
        self.client = None

    async def __aenter__(self):
        self.client = httpx.AsyncClient(timeout=5.0, headers={"User-Agent": "Mozilla/5.0"})
        return self
    
    async def __aexit__(self, *args):
        await self.client.aclose()
        self.client = None

    async def fetch(self, ticker):
        if ticker in self.cache:
            return self.cache[ticker], "cache"
        async with self.sem:
            if ticker in self.cache:
                return self.cache[ticker], "cache"
            try:
                response = await self.client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}")
                response.raise_for_status()
                price = float(response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"])
                self.cache[ticker] = price
                return price, "live"
            except (httpx.HTTPError, KeyError, IndexError):
                print(f"Error fetching {ticker}")
                return None, "error"
            
    async def fetch_all(self, tickers):
        tasks = [self.fetch(t) for t in tickers]
        return await asyncio.gather(*tasks)
    
    async def report(self, tickers):
        results = await self.fetch_all(tickers)
        console = Console()
        table = Table(title="Stock Prices")
        table.add_column("Ticker", justify="center")
        table.add_column("Price", justify="right")
        table.add_column("Source", justify="center")
        for t, (p, source) in zip(tickers, results):
            price_str = f"${p:.2f}" if p is not None else "N/A"
            source_str = f"[green]{source}[/green]" if source == "live" else f"[yellow]{source}[/yellow]"
            table.add_row(t, price_str, source_str)
        console.print(table)

async def main():
    tickers = ["AAPL", "TSLA", "NVDA", "GOOGL", "AAPL", "TSLA"]
    async with FintechAggregator(max_concurrent=3) as agg:
        await agg.report(tickers)
        print(f"Cache hits: {len(tickers) - len(agg.cache)}")

if __name__ == "__main__":
    asyncio.run(main())
