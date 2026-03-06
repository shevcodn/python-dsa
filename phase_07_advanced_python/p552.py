import asyncio
import time

async def fetch_price(ticker, delay):
    print(f"Fetching price for {ticker}...")
    await asyncio.sleep(delay)
    price = 100.0
    print(f"Price for {ticker}: {price}")
    return price

async def main():
    start = time.time()
    print(f"Fetching prices for AAPL...")
    await fetch_price("AAPL", 1)
    print(f"Fetching prices for NVDA...")
    await fetch_price("NVDA", 1)

    return time.time() - start

if __name__ == "__main__":
    total_time = asyncio.run(main())
    print(f"Total time taken: {total_time:.2f} seconds")
    