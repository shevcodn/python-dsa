import os
import asyncio
import asyncpg
from datetime import datetime

async def migrate_v1(conn):
    await conn.execute("DROP TABLE IF EXISTS users")
    await conn.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT NOT NULL)")

async def migrate_v2(conn):
    await conn.execute("ALTER TABLE users ADD COLUMN email TEXT")

async def migrate_v3(conn):
    await conn.execute("ALTER TABLE users ADD COLUMN created_at TIMESTAMP DEFAULT NOW()")

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )
    await migrate_v1(conn)
    await conn.execute("INSERT INTO users (id, name) VALUES ($1, $2)", 1, "Denis")
    fetch = await conn.fetch("SELECT * FROM users")
    print("Users after v1 migration:", fetch)
    await migrate_v2(conn)
    await conn.execute("UPDATE users SET email = $1 WHERE id = $2", "denis@example.com", 1)
    row = await conn.fetchrow("SELECT * FROM users WHERE id = $1", 1)
    print("User after v2 migration:", row)
    await migrate_v3(conn)
    await conn.execute("UPDATE users SET created_at = $1 WHERE id = $2", datetime(2024, 1, 1, 12, 0, 0), 1)
    row = await conn.fetchrow("SELECT * FROM users WHERE id = $1", 1)
    print("User after migrations:", row)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())