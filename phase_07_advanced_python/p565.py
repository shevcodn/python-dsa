import asyncio

async def fetch_page(sem, page):
    async with sem:
        print(f"Fetching page {page}...")
        await asyncio.sleep(1)
        print(f"Finished fetching page {page}")
        return {"page": page, "content": f"Content of page {page}"}
    
async def main():
    sem = asyncio.Semaphore(3)
    pages = [1, 2, 3, 4, 5]
    results = await asyncio.gather(*[fetch_page(sem, p) for p in pages])
    print("All pages fetched:")
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

    