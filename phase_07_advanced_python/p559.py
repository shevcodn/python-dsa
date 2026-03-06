import asyncio

async def producer(queue):
    tickers = ["AAPL", "NVDA", "TSLA"]
    for ticker in tickers:
        await queue.put(ticker)
        print(f"Produced {ticker}")
        await asyncio.sleep(0.3)
    await queue.put(None)

async def consumer(queue):
    while True:
        ticker = await queue.get()
        if ticker is None:
            break
        print(f"Consumed {ticker}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue),
    )

if __name__ == "__main__":
    asyncio.run(main())
    