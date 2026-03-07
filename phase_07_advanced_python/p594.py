import asyncio
import json
import httpx
import aiofiles


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

    async def add_position(self, ticker, shares, avg_price):
        self.portfolio[ticker] = {"shares": shares, "avg_price": avg_price}

    async def save_portfolio(self, filename):
        async with aiofiles.open(filename, "w") as f:
            await f.write(json.dumps(self.portfolio, indent=2))
        print(f"Saved to {filename}")

    async def load_portfolio(self, filename):
        async with aiofiles.open(filename, "r") as f:
            content = await f.read()
        self.portfolio = json.loads(content)
        print(f"Loaded from {filename}: {self.portfolio}")


async def main():
    async with StockClient() as client:
        await client.add_position("AAPL", 10, 150.0)
        await client.add_position("TSLA", 5, 300.0)
        await client.add_position("NVDA", 8, 120.0)
        await client.save_portfolio("portfolio.json")

    async with StockClient() as client2:
        await client2.load_portfolio("portfolio.json")


if __name__ == "__main__":
    asyncio.run(main())
