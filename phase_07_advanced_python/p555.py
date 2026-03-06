import asyncio 
import time

async def fetch_price(ticker, delay):
    print(f"Fetching price for {ticker}...")
    await asyncio.sleep(delay)
    price = 150.0
    print(f"Price for {ticker}: {price}")
    return price

async def main():
    start = time.time()

    results = await asyncio.gather(
        fetch_price("AAPL", 1),
        fetch_price("NVDA", 1),
        fetch_price("TSLA", 1)
    )

    total_time = time.time() - start
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())