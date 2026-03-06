import asyncio
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.text[:100]}")
        return response.text
    
async def main():
    await fetch("https://httpbin.org/get")

asyncio.run(main())