import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )

    await conn.execute("DROP TABLE IF EXISTS orders CASCADE")
    await conn.execute("CREATE TABLE IF NOT EXISTS orders (id SERIAL PRIMARY KEY, product TEXT NOT NULL, quantity REAL NOT NULL, price REAL NOT NULL, created_at TIMESTAMP DEFAULT NOW())")
    stmt = await conn.prepare("INSERT INTO orders (product, quantity, price) VALUES ($1, $2, $3)")
    await stmt.executemany([
        ("Laptop", 1, 1200.0),
        ("Phone", 2, 800.0),
        ("Tablet", 3, 600.0),
        ("Headphones", 4, 150.0),
        ("Monitor", 5, 300.0)
    ])
    select = await conn.prepare("SELECT * FROM orders WHERE price > $1")
    rows = await select.fetch(500.0)
    print("Orders with price greater than 500.0:", rows)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
    