import asyncio
import httpx

async def stream_download(url):
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            print(f"Status code: {response.status_code}")
            async for chunk in response.aiter_text():
                print(chunk, end="")
            
async def main():
    await stream_download("https://httpbin.org/stream/5")

if __name__ == "__main__":
    asyncio.run(main())