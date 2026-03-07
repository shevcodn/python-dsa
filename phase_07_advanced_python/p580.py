import asyncio
import httpx

async def create_order(client, order):
    headers = {"Content-Type": "application/json"}
    response = await client.post("https://httpbin.org/post", json=order, headers=headers)
    return response.json()["json"]

async def main():
    tickers = ["AAPL", "TSLA"]
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*[create_order(client, {"ticker": t, "quantity": 10, "side": "buy"}) for t in tickers])
    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
