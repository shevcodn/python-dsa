import asyncio
import random

class StockFeed:
    def __init__(self, ticker, count):
        self.ticker = ticker
        self.count = count
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.count:
            raise StopAsyncIteration
        await asyncio.sleep(0.3)
        self.current += 1
        return f"{self.ticker}: ${random.randint(100, 500)}"

async def main():
    async for price in StockFeed("TSLA", 4):
        print(price)

if __name__ == "__main__":
    asyncio.run(main())
