import asyncio 

async def get_price(ticker):
    print(f"Fetching price for {ticker}...")
    await asyncio.sleep(1)
    return 150.0

async def main():
    print("Starting to fetch price...")
    price = await get_price("AAPL")
    print(f"The price of AAPL is {price}")
if __name__ == "__main__":
    asyncio.run(main())