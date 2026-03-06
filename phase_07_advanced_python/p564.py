import asyncio 

async def fetch_data(source, delay):
    print(f"fetching data from {source}...")
    await asyncio.sleep(delay)
    print(f"data from {source} fetched!")
    return {"source": source, "data": f"sample data from {source}"}

async def run_gather():
    results = await asyncio.gather(
        fetch_data("Source A", delay=1),
        fetch_data("Source B", delay=1),
        fetch_data("Source C", delay=1)
    )
    print("All data fetched:")
    for result in results:
        print(result)

async def run_wait():
    task1 = asyncio.create_task(fetch_data("Source A", delay=1))
    task2 = asyncio.create_task(fetch_data("Source B", delay=1))
    task3 = asyncio.create_task(fetch_data("Source C", delay=1))

    done, pending = await asyncio.wait([task1, task2, task3], return_when=asyncio.FIRST_COMPLETED)
    print("First completed task:")
    first = done.pop()
    print(first.result())
    for task in pending:
        task.cancel()

if __name__ == "__main__":
    asyncio.run(run_gather())
    asyncio.run(run_wait())