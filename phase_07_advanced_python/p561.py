import asyncio

balance = 1000

async def withdraw(amount, lock):
    global balance
    async with lock:
        print(f"Widtrawing {amount}...")
        await asyncio.sleep(0.1)
        balance -= amount
        print(f"New balance: {balance}")

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(
        withdraw(200, lock),
        withdraw(300, lock),
        withdraw(150, lock)
    )
    print(f"Final balance: {balance}")

if __name__ == "__main__":
    asyncio.run(main())