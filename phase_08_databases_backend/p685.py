import asyncio
import asyncpg

async def main():
    pool = await asyncpg.create_pool(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777",
        min_size=1, max_size=5
    )

    async with pool.acquire() as conn:
        await conn.execute("DROP TABLE IF EXISTS products CASCADE")
        await conn.execute("""
            CREATE TABLE products (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL CHECK (price > 0),
                stock INT DEFAULT 0 CHECK (stock >= 0),
                category TEXT NOT NULL DEFAULT 'general'
            )
        """)

        await conn.execute("INSERT INTO products (name, price, stock, category) VALUES ($1, $2, $3, $4)", "Laptop", 999.99, 10, "Electronics")

        try:
            await conn.execute("INSERT INTO products (name, price, stock, category) VALUES ($1, $2, $3, $4)", "Broken", -10.0, 5, "Electronics")
        except asyncpg.exceptions.CheckViolationError as e:
            print(f"Price error: {e}")

        try:
            await conn.execute("INSERT INTO products (name, price, stock, category) VALUES ($1, $2, $3, $4)", "Broken2", 10.0, -5, "Electronics")
        except asyncpg.exceptions.CheckViolationError as e:
            print(f"Stock error: {e}")

        rows = await conn.fetch("SELECT * FROM products")
        print("Valid products:", rows)

    await pool.close()

if __name__ == "__main__":
    asyncio.run(main())
