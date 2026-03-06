import asyncio
import random

async def price_stream(ticker, count):
    for _ in range(count):
        await asyncio.sleep(0.5)
        yield f"{ticker}: ${random.randint(100, 500)}"


async def main():
    async for price in price_stream("AAPL", 5):
        print(price)


if __name__ == "__main__":
    asyncio.run(main())
