import asyncio

async def deposit(lock, account, amount):
    async with lock:
        print(f"Depositing {amount}...")
        await asyncio.sleep(0.1)
        account['balance'] += amount
        print(f"New balance: {account['balance']}")
        await asyncio.sleep(0.1)
        print(f"Deposited {amount} successfully!")
        return account['balance']
    

async def main():
    lock = asyncio.Lock()
    account = {'balance': 0}
    await asyncio.gather(
        deposit(lock, account, 100),
        deposit(lock, account, 200),
        deposit(lock, account, 150),
        deposit(lock, account, 300),
        deposit(lock, account, 50)
    )

if __name__ == "__main__":
    asyncio.run(main())