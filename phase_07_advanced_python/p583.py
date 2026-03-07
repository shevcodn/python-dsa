import asyncio
import httpx

async def fetch(client, sem, ticker):
    async with sem:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers=headers)
        price = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return f"{ticker}: ${price}"
    
async def main():
    sem = asyncio.Semaphore(3)
    async with httpx.AsyncClient(timeout=5.0) as client:
        tickers = ["AAPL", "TSLA", "NVDA", "GOOGL", "AMZN", "META"]
        result = await asyncio.gather(*[fetch(client, sem, t) for t in tickers])
        for r in result:
            print(r)

if __name__ == "__main__":
    asyncio.run(main())
