import asyncio
import httpx

async def fetch_cached(client, ticker, cache):
    if ticker in cache:
        print(f"Cache hit for {ticker}")
        return cache[ticker]
    else:
        response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
        cache[ticker] = data
        print(f"Fetched {ticker} and stored in cache")
        return data
    
async def main():
    cache = {}
    async with httpx.AsyncClient(timeout=5.0) as client:
        tickers = ["AAPL", "TSLA", "NVDA", "GOOGL", "AAPL", "TSLA"]
        results = await asyncio.gather(*[fetch_cached(client, t, cache) for t in tickers])
        for r in results:
            print(r)
        print(f"Cache hits saved {len(tickers) - len(cache)} requests")

if __name__ == "__main__":
    asyncio.run(main())