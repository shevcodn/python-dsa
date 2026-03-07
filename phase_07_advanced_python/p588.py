import asyncio
import httpx
import respx


async def fetch_price(ticker):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}", headers={"User-Agent": "Mozilla/5.0"}, timeout=5.0)
        price = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return f"{ticker}: ${price}"

@respx.mock
async def test_fetch_price():
    respx.get("https://query1.finance.yahoo.com/v8/finance/chart/AAPL").mock(return_value=httpx.Response(200, json={"chart": {"result": [{"meta": {"regularMarketPrice": 150.0}}]}}))
    result = await fetch_price("AAPL")
    assert result == "AAPL: $150.0"
    print("Test passed:", result)

async def main():
    await test_fetch_price()

if __name__ == "__main__":
    asyncio.run(main())
