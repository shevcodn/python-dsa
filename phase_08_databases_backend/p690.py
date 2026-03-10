import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )

    await conn.execute("DROP TABLE IF EXISTS sales")
    await conn.execute("CREATE TABLE IF NOT EXISTS sales (id SERIAL PRIMARY KEY, seller INT, amount REAL NOT NULL, month INT NOT NULL)")
    await conn.execute("INSERT INTO transactions (user_id, amount, status) VALUES ($1, $2, $3)", 1, 100.0, "pending")
    await conn.execute("INSERT INTO transactions (user_id, amount, status) VALUES ($1, $2, $3)", 1, 150.0, "pending")
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 100.0, 1)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 150.0, 2)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 200.0, 3)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 250.0, 4)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 300.0, 5)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 350.0, 6)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 400.0, 7)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 450.0, 8)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 500.0, 9)
    await conn.execute("INSERT INTO sales (seller, amount, month) VALUES ($1, $2, $3)", 1, 550.0, 10)
    rank = await conn.fetch("SELECT seller, amount, month, RANK() OVER (ORDER BY amount DESC) FROM sales")
    print("Rank:", rank)
    sum = await conn.fetch("SELECT seller, month, SUM(amount) OVER (PARTITION BY seller ORDER BY MONTH) FROM sales")
    print("Sum:", sum)
    lag = await conn.fetch("SELECT seller, month, amount, LAG(amount) OVER (ORDER BY month) FROM sales")
    print("Lag:", lag)
    lead = await conn.fetch("SELECT seller, month, amount, LEAD(amount) OVER (ORDER BY month) FROM sales")
    print("Lead:", lead)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())