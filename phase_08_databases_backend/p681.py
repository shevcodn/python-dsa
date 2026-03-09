import asyncio
import asyncpg

async def main():
    pool = await asyncpg.create_pool(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777",
        min_size=1, max_size=5
    )

    async with pool.acquire() as conn:
        await conn.execute("DROP TABLE IF EXISTS orders")
        await conn.execute("CREATE TABLE orders (id SERIAL PRIMARY KEY, customer TEXT NOT NULL, amount REAL NOT NULL, status TEXT NOT NULL)")

        data = [(f"customer_{i}", float(i * 10), "completed" if i % 2 == 0 else "pending") for i in range(1000)]
        await conn.executemany("INSERT INTO orders (customer, amount, status) VALUES ($1, $2, $3)", data)

        print("=== WITHOUT INDEX ===")
        rows = await conn.fetch("EXPLAIN ANALYZE SELECT * FROM orders WHERE customer = $1", "customer_500")
        for row in rows:
            print(row[0])

        await conn.execute("CREATE INDEX idx_customer ON orders (customer)")

        print("\n=== WITH INDEX ===")
        rows = await conn.fetch("EXPLAIN ANALYZE SELECT * FROM orders WHERE customer = $1", "customer_500")
        for row in rows:
            print(row[0])

    await pool.close()

if __name__ == "__main__":
    asyncio.run(main())