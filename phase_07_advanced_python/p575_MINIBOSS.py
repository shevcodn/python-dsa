import asyncio
import random
import time

async def fetch_price(ticker, sem, lock, stats):
    async with sem:
        print(f"Fetching price for {ticker}...")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        if random.random() < 0.2:
            raise Exception(f"Failed to fetch price for {ticker}")
        async with lock:
            stats['success'] += 1
        return f"{ticker}: ${random.randint(100, 500)}"
    
async def monitor(tickers, ready_event):
    await ready_event.wait()
    sem = asyncio.Semaphore(3)
    lock = asyncio.Lock()
    stats = {'success': 0, "errors": 0}
    results = await asyncio.gather(*[fetch_price(t, sem, lock, stats) for t in tickers], return_exceptions=True)
    for r in results:
        print(r)
    print(stats)

async def launcher(ready_event):
    print("Launcher is preparing...")
    await asyncio.sleep(1)
    print("Market Open!")
    ready_event.set()

async def main():
    tickers = ["AAPL", "NVDA", "TSLA", "GOOG", "AMZN"]
    ready_event = asyncio.Event()
    await asyncio.gather(
        monitor(tickers, ready_event),
        launcher(ready_event)
    )

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Total execution time: {time.time() - start_time:.2f} seconds")