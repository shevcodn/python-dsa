import os
import asyncio
import asyncpg

async def get_user(pool, user_id):
    async with pool.acquire() as conn:
        return await conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)

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
        await conn.execute("INSERT INTO users (name, balance) VALUES ($1, $2)", "Nastya", 300.0)

    results = await asyncio.gather(
        get_user(pool, 1),
        get_user(pool, 2),
        get_user(pool, 3)
    )
    print("Results:", results)
    await pool.close()

if __name__ == "__main__":
    asyncio.run(main())