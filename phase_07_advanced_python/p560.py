import asyncio
import random

async def fetch_price(ticker):
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)
    if random.random() < 0.3:
        raise Exception(f"Failed to fetch price for {ticker}")
    return f"{ticker}: ${random.randint(100, 500):.2f}"

async def safe_fetch(ticker):
    try:
        result = await asyncio.wait_for(fetch_price(ticker), timeout=1.5)
        print(f"Successfully fetched price: {result}")
    except asyncio.TimeoutError:
        print(f"Timeout while fetching price for {ticker}")
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")

async def main():
    tickers = ["AAPL", "NVDA", "TSLA", "GOOG", "AMZN"]
    await asyncio.gather(*[safe_fetch(t) for t in tickers])

if __name__ == "__main__":
    asyncio.run(main())