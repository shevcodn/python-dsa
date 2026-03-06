import asyncio
import random

async def producer(q1):
    tickers = ["AAPL", "NVDA", "TSLA", "GOOGL"]
    for ticker in tickers:
        await q1.put(ticker)
        print(f"Produced {ticker}")
        await asyncio.sleep(0.3)
    await q1.put(None)

async def processor(q1, q2):
    while True:
        ticker = await q1.get()
        if ticker is None:
            await q2.put(None)
            break
        price = f"{ticker}: ${random.randint(100, 500)}"
        await q2.put(price)
        print(f"Processed {ticker}")
        await asyncio.sleep(0.5)
        q1.task_done()
    await q2.put(None)

async def saver(q2):
    while True:
        price = await q2.get()
        if price is None:
            break
        print(f"Saved {price}")
        await asyncio.sleep(0.2)
        q2.task_done()

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    await asyncio.gather(
        producer(q1),
        processor(q1, q2),
        saver(q2)
    )

if __name__ == "__main__":
    asyncio.run(main())