import os
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )

    await conn.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    await conn.execute("DROP TABLE IF EXISTS users")
    await conn.execute("""
        CREATE TABLE users (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    await conn.execute("INSERT INTO users (name, email) VALUES ($1, $2)", "Denis", "denis@example.com")
    await conn.execute("INSERT INTO users (name, email) VALUES ($1, $2)", "Alice", "alice@example.com")

    rows = await conn.fetch("SELECT * FROM users")
    print("All users:", rows)

    first_id = rows[0]["id"]
    row = await conn.fetchrow("SELECT * FROM users WHERE id = $1", first_id)
    print("User by UUID:", row)

    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
