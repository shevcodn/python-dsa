import asyncio

async def worker(event, name):
    await event.wait()
    print(f"{name} started working")

async def loader(event):
    await asyncio.sleep(2)
    print("Data loaded!")
    event.set()

async def main():
    event = asyncio.Event()
    await asyncio.gather(
        loader(event),
        worker(event, "worker_1"),
        worker(event, "worker_2"),
        worker(event, "worker_3")
    )

if __name__ == "__main__":
    asyncio.run(main())
    