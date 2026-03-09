import asyncio 
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
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
        executed = await conn.execute("UPDATE users SET BALANCE = $1 WHERE id = $2", 150.0, 1)
        print("Update result:", executed)
        fetchrow = await conn.fetchrow("SELECT * FROM users where id = $1", 1)
        print("User with ID 1 after update:", fetchrow)
        executed = await conn.execute("DELETE FROM users WHERE id = $1", 2)
        print("Delete result:", executed)
        rows = await conn.fetch("SELECT * FROM users")
        print("All users after deletion:", rows)
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
