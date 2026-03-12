import os
import asyncio
import asyncpg

async def main():
    pool = await asyncpg.create_pool(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password"),
        min_size=1, max_size=5
    )

    async with pool.acquire() as conn:
        await conn.execute("DROP TABLE IF EXISTS users")
        await conn.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT NOT NULL, balance REAL NOT NULL)")
        await conn.execute("INSERT INTO users (name, balance) VALUES ($1, $2)", "Denis", 100.0)
        await conn.execute("INSERT INTO users (name, balance) VALUES ($1, $2)", "Alice", 200.0)
        rows = await conn.fetch("SELECT * FROM users")
        print("All users:", rows)

    await pool.close()

if __name__ == "__main__":
    asyncio.run(main())