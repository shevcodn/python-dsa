import asyncio
import httpx

async def fetch_page(client, page, limit=5):
    params = {"page": page, "limit": limit}
    response = await client.get("https://httpbin.org/get", params=params)
    return response.json()["args"]

async def fetch_all_pages(client, total_pages=3):
    tasks = [fetch_page(client, page) for page in range(1, total_pages + 1)]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    async with httpx.AsyncClient() as client:
        all_pages = await fetch_all_pages(client)
        for page in all_pages:
            print(page)

if __name__ == "__main__":
    asyncio.run(main())
