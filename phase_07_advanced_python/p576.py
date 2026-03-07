import asyncio
import httpx

async def get_price(ticker):
    headers = {"User-Agent": "Mozilla/5.0"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers=headers)
        return response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]

async def main():
    tickers = ["AAPL", "TSLA"]
    tasks = [asyncio.create_task(get_price(t)) for t in tickers]
    for task in tasks:
        price = await task
        print(f"Price for {tickers[tasks.index(task)]}: {price}")

if __name__ == "__main__":
    asyncio.run(main())
