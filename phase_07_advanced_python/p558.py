import asyncio 

async def slow_request(ticker):
    print(f"Fetching price for {ticker}...")
    await asyncio.sleep(5)
    price = 150.0
    print(f"Price for {ticker}: {price}")
    return price

async def main():
    try:
        price = await asyncio.wait_for(slow_request("AAPL"), timeout=2.0)
        print(f"Received price: {price}")
    except asyncio.TimeoutError:
        print("Request timed out!")

if __name__ == "__main__":
    asyncio.run(main())