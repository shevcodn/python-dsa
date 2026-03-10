import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )

    await conn.execute("DROP TABLE IF EXISTS users CASCADE")
    await conn.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT NOT NULL, metadata JSONB)")
    await conn.execute("INSERT INTO users (name, metadata) VALUES ($1, $2)", "Denis", '{"age": 22, "city": "Toronto", "skills": ["Python", "SQL"]}')
    await conn.execute("INSERT INTO users (name, metadata) VALUES ($1, $2)", "Alice", '{"age": 25, "city": "Vancouver"}')
    fetch = await conn.fetch("SELECT * FROM users")
    print("All users:", fetch)
    fetchrow = await conn.fetchrow("SELECT * FROM users WHERE metadata->>'city' = $1", "Toronto")
    print("User from Toronto:", fetchrow)

    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())