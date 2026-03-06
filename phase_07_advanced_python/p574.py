import asyncio


async def worker(name, event, sem, lock, counter):
    print(f"{name} is waiting for the event...")
    await event.wait()
    print(f"{name} has started working!")
    async with sem:
        print(f"{name} is working...")
        await asyncio.sleep(1)
        async with lock:
            counter[0] += 1
            print(f"{name} has finished working! Counter: {counter[0]}")
    
async def starter(event):
    print("Starter is doing some setup...")
    await asyncio.sleep(1)
    print("GO!")
    event.set()

async def main():
    event = asyncio.Event()
    sem = asyncio.Semaphore(2)
    lock = asyncio.Lock()
    counter = [0]

    workers = [worker(f"Worker-{i}", event, sem, lock, counter) for i in range(5)]
    starter_task = starter(event)

    await asyncio.gather(starter_task, *workers)

if __name__ == "__main__":
    asyncio.run(main())