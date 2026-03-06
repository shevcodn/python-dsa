import asyncio
import time

async def async_wait():
    print("Starting async wait...")
    await asyncio.sleep(1)
    print("Finished async wait!")

async def blocking_wait():
    print("Starting blocking wait...")
    time.sleep(1)
    print("Finished blocking wait!")

async def main():
    await asyncio.gather(
        async_wait(), blocking_wait()
    )

if __name__ == "__main__":
    asyncio.run(main())