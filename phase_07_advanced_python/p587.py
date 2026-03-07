import asyncio
import httpx

async def fetch_price(client, ticker):
    print(f"Fetching price for {ticker}...")
    await asyncio.sleep(1)
    header = {"User-Agent": "Mozilla/5.0"}
    response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers=header)
    price = response.json()['chart']['result'][0]['meta']['regularMarketPrice']
    return price

async def fetch_info(client, ticker):
    response = await client.get(f"https://httpbin.org/get", params={"ticker": ticker})
    return {"ticker": ticker, "source": "httpbin"}

async def fetch_all(client, ticker):
    price, info = await asyncio.gather(fetch_price(client, ticker), fetch_info(client, ticker))
    return {"ticker": ticker, "price": price, "info": info}

async def main():
    async with httpx.AsyncClient(timeout=5.0) as client:
        tickers = ["AAPL", "TSLA", "NVDA"]
        results = await asyncio.gather(*[fetch_all(client, t) for t in tickers])
        for r in results:
            print(r)

if __name__ == "__main__":
    asyncio.run(main())