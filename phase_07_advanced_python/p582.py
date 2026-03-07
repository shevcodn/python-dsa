import asyncio
import httpx

async def fetch_with_retry(client, ticker, retries=3):
    headers = {"User-Agent": "Mozilla/5.0"}
    for attempt in range(retries):
        try:
            response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers=headers)
            response.raise_for_status()
            price = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
            return f"{ticker}: ${price}"
        except (httpx.HTTPError, KeyError) as e:
            print(f"Attempt {attempt + 1} failed for {ticker}: {e}")
            if attempt == retries - 1:
                return f"{ticker}: Failed to fetch price after {retries} attempts"
            await asyncio.sleep(1)

async def main():
    async with httpx.AsyncClient(timeout=5.0) as client:
        tickers = ["AAPL", "TSLA", "NVDA", "GOOGL"]
        results = await asyncio.gather(*[fetch_with_retry(client, t) for t in tickers])
        for r in results:
            print(r)

if __name__ == "__main__":
    asyncio.run(main())

    