import asyncio
import httpx

async def fetch(client, ticker):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers=headers)
    price = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
    return f"{ticker}: ${price}"

async def main():
    async with httpx.AsyncClient() as client:
        tickers = ["AAPL", "TSLA", "NVDA", "GOOGL"]
        results = await asyncio.gather(*[fetch(client, t) for t in tickers])
        for r in results:
            print(r)

if __name__ == "__main__":
    asyncio.run(main())