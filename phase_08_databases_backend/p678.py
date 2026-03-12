import os
import asyncio
import asyncpg

async def transfer(conn, from_id, to_id, amount):
    async with conn.transaction():
        from_user = await conn.fetchrow("SELECT * FROM users WHERE id = $1", from_id)
        if from_user["balance"] < amount:
            raise ValueError("Insufficient funds")
        new_balance = from_user["balance"] - amount
        await conn.execute("UPDATE users SET balance = $1 WHERE id = $2", new_balance, from_id)
        to_user = await conn.fetchrow("SELECT * FROM users WHERE id = $1", to_id)
        new_balance = to_user["balance"] + amount
        await conn.execute("UPDATE users SET balance = $1 WHERE id = $2", new_balance, to_id)
        print(f"Transfer {amount} complete.")

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )
    try:
        await conn.execute("DROP TABLE IF EXISTS users")
        await conn.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT NOT NULL, balance REAL NOT NULL)")
        await conn.execute("INSERT INTO users (name, balance) VALUES ($1, $2)", "Denis", 1000.0)
        await conn.execute("INSERT INTO users (name, balance) VALUES ($1, $2)", "Alice", 500.0)

        await transfer(conn, 1, 2, 300)

        try:
            await transfer(conn, 1, 2, 5000)
        except ValueError as e:
            print(f"Transfer failed: {e}")

        rows = await conn.fetch("SELECT * FROM users")
        print("Final:", rows)
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(main())