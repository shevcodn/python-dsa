import asyncio
import httpx

async def fetch(client, ticker, cache, sem, retries=3):
    async with sem:
        if ticker in cache:
            print(f"Cache hit for {ticker}")
            return cache[ticker]
        
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        
        for attempt in range(retries):
            if ticker in cache:
                print(f"Cache hit for {ticker} on retry {attempt + 1}")
                return cache[ticker]
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                price = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
                cache[ticker] = f"{ticker}: ${price}"
                print(f"Fetched {ticker} and stored in cache")
                return cache[ticker]
            except (httpx.HTTPError, KeyError) as e:
                print(f"Attempt {attempt + 1} failed for {ticker}: {e}")
                if attempt == retries - 1:
                    return f"{ticker}: Failed to fetch price after {retries} attempts"
                await asyncio.sleep(1)

async def main():
    cache = {}
    sem = asyncio.Semaphore(3)
    async with httpx.AsyncClient(timeout=5.0) as client:
        tickers = ["AAPL", "TSLA", "NVDA", "GOOGL", "AAPL", "TSLA"]
        results = await asyncio.gather(*[fetch(client, t, cache, sem) for t in tickers])
        for r in results:
            print(r)
        print(f"Cache hits saved {len(tickers) - len(cache)} requests")

if __name__ == "__main__":
    asyncio.run(main())