import asyncio

async def fetch(ticker, semaphore):
    async with semaphore:
        print(f"Fetching price for {ticker}...")
        await asyncio.sleep(1)
        price = 150.0
        print(f"Price for {ticker}: {price}")
        return price
    
async def main():
    semaphore = asyncio.Semaphore(2)

    tickers = ["AAPL", "NVDA", "TSLA", "MSFT", "GOOGL"]
    await asyncio.gather(*[fetch(t, semaphore) for t in tickers])

if __name__ == "__main__":
    asyncio.run(main())