import asyncio
import httpx

async def fetch(client, ticker):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers=headers)
        return response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
    except httpx.TimeoutException:
        return f"{ticker}: Timeout"
    except Exception as e:
        return f"{ticker}: Error - {e}"
    finally:
        print(f"Finished fetching {ticker}")
    
async def main():
    async with httpx.AsyncClient(timeout=5.0) as client:
        tickers = ["AAPL", "TSLA", "NVDA", "GOOGL"]
        results = await asyncio.gather(*[fetch(client, t) for t in tickers])
        for r in results:
            print(r)

if __name__ == "__main__":
    asyncio.run(main())