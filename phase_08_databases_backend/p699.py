import os
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )

    await conn.execute("DROP TABLE IF EXISTS accounts CASCADE")
    await conn.execute("CREATE TABLE accounts (id SERIAL PRIMARY KEY, name TEXT NOT NULL, balance REAL NOT NULL)")
    await conn.execute("INSERT INTO accounts (name, balance) VALUES ($1, $2)", "Alice", 1000.0)
    await conn.execute("INSERT INTO accounts (name, balance) VALUES ($1, $2)", "Bob", 500.0)

    async with conn.transaction():
        await conn.execute("UPDATE accounts SET balance = 800.0 WHERE name = $1", "Alice")
        try:
            async with conn.transaction():
                await conn.execute("UPDATE accounts SET balance = 700.0 WHERE name = $1", "Bob")
                raise ValueError("Something went wrong")
        except ValueError:
            print("Savepoint rolled back")

    rows = await conn.fetch("SELECT * FROM accounts")
    print("Final states:", rows)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
