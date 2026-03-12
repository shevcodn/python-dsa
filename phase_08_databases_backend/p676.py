import os
import asyncio 
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )
    try:
        await conn.execute("DROP TABLE IF EXISTS users")
        await conn.execute("CREATE TABLE IF NOT EXISTS users" \
        "(id SERIAL PRIMARY KEY, name TEXT NOT NULL, balance REAL NOT NULL)")
        await conn.execute("INSERT INTO users (name, balance) VALUES ($1, $2)", "Denis", 100.0)
        await conn.execute("INSERT INTO users (name, balance) VALUES ($1, $2)", "Alice", 200.0)
        rows = await conn.fetch("SELECT * FROM users")
        print("All users:", rows)
        fetchrow = await conn.fetchrow("SELECT * FROM users WHERE id = $1", 1)
        print("User with ID 1:", fetchrow)
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
