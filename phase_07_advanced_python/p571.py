import asyncio
import random

async def fetch_price(ticker):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return f"{ticker}: ${random.randint(100, 500)}"

async def main():
    tickers = ["AAPL", "NVDA", "TSLA"]
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for t in tickers:
            tasks.append(tg.create_task(fetch_price(t)))
    for task in tasks:
        print(task.result())

if __name__ == "__main__":
    asyncio.run(main())
