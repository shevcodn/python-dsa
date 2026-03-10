import asyncio
import asyncpg
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    balance: float = 0.0


class UserRepository:
    def __init__(self, conn):
        self.conn = conn

    async def create(self, name, email, balance) -> int:
        row = await self.conn.fetchrow("INSERT INTO users (name, email, balance) VALUES ($1, $2, $3) RETURNING id", name, email, balance)
        return row['id']
    
    async def find_by_id(self, user_id) -> User:
        row = await self.conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)
        if row:
            return User(id=row['id'], name=row['name'], balance=row['balance'])
        return None
    
    async def find_all(self) -> list[User]:
        rows = await self.conn.fetch("SELECT * FROM users")
        return [User(id=row['id'], name=row['name'], balance=row['balance']) for row in rows]
    
async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )
    try:
        await conn.execute("DROP TABLE IF EXISTS users")
        await conn.execute("""
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                balance REAL NOT NULL
            )
        """)
        repo = UserRepository(conn)
        user_id = await repo.create("Denis", "denis@example.com", 100.0)
        print(f"Created user with ID: {user_id}")
        user = await repo.find_by_id(user_id)
        print(f"Found user: {user}")
        all_users = await repo.find_all()
        print(f"All users: {all_users}")
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(main())