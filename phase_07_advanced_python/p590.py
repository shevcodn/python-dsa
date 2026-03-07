import asyncio
import httpx

class APISession:
    def __init__(self, base_url):
        self.base_url = base_url
        self.client = None
        self.request_count = 0

    async def __aenter__(self):
        self.client = httpx.AsyncClient()
        return self

    async def __aexit__(self, *args):
        await self.client.aclose()

    async def get(self, path, **kwargs):
        self.request_count += 1
        print(f"Request #{self.request_count}: {path}")
        response = await self.client.get(self.base_url + path, **kwargs)
        return response

async def main():
    headers = {"User-Agent": "Mozilla/5.0"}
    async with APISession("https://query1.finance.yahoo.com") as session:
        for ticker in ["AAPL", "TSLA", "NVDA"]:
            response = await session.get(f"/v8/finance/chart/{ticker}", headers=headers, timeout=5.0)
            price = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
            print(f"{ticker}: ${price}")
        print(f"Total requests: {session.request_count}")

if __name__ == "__main__":
    asyncio.run(main())
