import asyncio
import httpx


class StockClient:
    BASE_URL = "https://query1.finance.yahoo.com"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    def __init__(self):
        self.client = None
        self.portfolio = {}

    async def __aenter__(self):
        self.client = httpx.AsyncClient(base_url=self.BASE_URL, headers=self.HEADERS)
        return self
    
    async def __aexit__(self, *args):
        await self.client.aclose()
        self.client = None

    async def get_price(self, ticker) -> float:
        response = await self.client.get(f"/v8/finance/chart/{ticker}", timeout=5.0)
        return float(response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"])
    
    async def get_prices(self, tickers) -> dict:
        prices = await asyncio.gather(*[self.get_price(t) for t in tickers])
        return {t: p for t, p in zip(tickers, prices) if p is not None}
    
async def main():
    async with StockClient() as client:
        tickers = ["AAPL", "TSLA", "NVDA", "GOOGL", "AMZN", "META"]
        prices = await client.get_prices(tickers)
        for ticker, price in prices.items():
            print(f"{ticker}: ${price}")
            client.portfolio[ticker] = price
        print(f"Portfolio: {client.portfolio}")
    
if __name__ == "__main__":
    asyncio.run(main())