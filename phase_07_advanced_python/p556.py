import asyncio
import time

async def fetch_price(ticker):
    print(f"Fetching price for {ticker}...")
    await asyncio.sleep(1)
    price = 150.0
    print(f"Price for {ticker}: {price}")
    return price

async def main():
    start = time.time()

    task1 = asyncio.create_task(fetch_price("AAPL"))
    task2 = asyncio.create_task(fetch_price("NVDA"))

    result1 = await task1
    result2 = await task2

    total_time = time.time() - start
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Results: {result1}, {result2}")

if __name__ == "__main__":
    asyncio.run(main())