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
        await conn.execute("DROP TABLE IF EXISTS orders")
        await conn.execute("DROP TABLE IF EXISTS users")
        await conn.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT NOT NULL)")
        await conn.execute("CREATE TABLE orders (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users(id) ON DELETE CASCADE, amount REAL NOT NULL)")
        await conn.execute("INSERT INTO users (name) VALUES ($1)", "Denis")
        await conn.execute("INSERT INTO users (name) VALUES ($1)", "Alice")
        await conn.execute("INSERT INTO orders (user_id, amount) VALUES ($1, $2)", 1, 100.0)
        await conn.execute("INSERT INTO orders (user_id, amount) VALUES ($1, $2)", 1, 150.0)
        fetch = await conn.fetch("SELECT * FROM orders")
        print("All orders:", fetch)
        await conn.execute("DELETE FROM users WHERE id = $1", 1)
        fetch = await conn.fetch("SELECT * FROM orders")
        print("All orders after deleting user with ID 1:", fetch)

    await pool.close()

if __name__ == "__main__":
    asyncio.run(main())