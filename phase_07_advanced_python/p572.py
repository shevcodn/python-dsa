import asyncio


def timer(func):
    async def wrapper(*args, **kwargs):
        start = asyncio.get_event_loop().time()
        result = await func(*args, **kwargs)
        end = asyncio.get_event_loop().time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper
    
@timer
async def fetch_data(ticker):
    print(f"Fetching data for {ticker}...")
    await asyncio.sleep(1)
    return f"{ticker}: $100.00"

async def main():
    await asyncio.gather(
        fetch_data("AAPL"),
        fetch_data("NVDA"),
        fetch_data("TSLA")
    )
    

if __name__ == "__main__":
    asyncio.run(main())