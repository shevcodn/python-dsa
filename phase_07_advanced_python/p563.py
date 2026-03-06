import asyncio

async def downloader(event):
    print("Starting download...")
    await asyncio.sleep(2)
    print("Download Complete!")
    event.set()

async def processor(event):
    print("Waiting for data...")
    await event.wait()
    print("Procesing data!")

async def main():
    event = asyncio.Event()
    await asyncio.gather(
        downloader(event),
        processor(event)
    )

if __name__ == "__main__":
    asyncio.run(main())