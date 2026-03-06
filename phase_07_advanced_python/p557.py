import asyncio

async def price_stream(tickers):
    for ticker in tickers:
        await asyncio.sleep(0.5)
        price = 150.0
        print(f"Price for {ticker}: {price}")
        yield ticker, price

async def main():
    tickers = ["AAPL", "NVDA", "TSLA", "MSFT"]
    async for ticker, price in price_stream(tickers):
        print(f"Received price for {ticker}: {price}")

if __name__ == "__main__":
    asyncio.run(main())