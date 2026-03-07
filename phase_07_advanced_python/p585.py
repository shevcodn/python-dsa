import asyncio
import httpx

class StockClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.client = None

    async def __aenter__(self):
        self.client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers)
        return self
    
    async def __aexit__(self, *args):
        await self.client.aclose()

    async def get_price(self, ticker):
        response = await self.client.get(f"/v8/finance/chart/{ticker}")
        return f"{ticker}: ${response.json()['chart']['result'][0]['meta']['regularMarketPrice']}"

    async def get_prices(self, tickers):
        return await asyncio.gather(*[self.get_price(t) for t in tickers])
    
async def main():
    async with StockClient(base_url="https://query1.finance.yahoo.com", headers={"User-Agent": "Mozilla/5.0"}) as client:
        prices = await client.get_prices(["AAPL", "TSLA", "NVDA"])
        for p in prices:
            print(p)

if __name__ == "__main__":
    asyncio.run(main())