import asyncio
import httpx

async def fetch_portfolio(client, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = await client.get("https://httpbin.org/bearer", headers=headers)
    return response.json()

async def fetch_with_custom_headers(client):
    headers = {"X-App-Name": "TradeLedger", "X-Version": "1.0"}
    response = await client.get("https://httpbin.org/headers", headers=headers)
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        token = "my_secret_token"
        portfolio = await fetch_portfolio(client, token)
        print("Portfolio Response:", portfolio)
        headers = await fetch_with_custom_headers(client)
        print("Custom Headers Response:", headers)

if __name__ == "__main__":
    asyncio.run(main())
