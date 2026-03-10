import asyncio
import asyncpg
from datetime import date

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )

    await conn.execute("DROP MATERIALIZED VIEW IF EXISTS sales_summary")
    await conn.execute("DROP TABLE IF EXISTS sales CASCADE")
    await conn.execute("CREATE TABLE sales (id SERIAL PRIMARY KEY, product TEXT NOT NULL, amount REAL NOT NULL, sold_at DATE NOT NULL)")
    await conn.execute("INSERT INTO sales (product, amount, sold_at) VALUES ($1, $2, $3)", "Laptop", 1200.0, date(2024, 1, 10))
    await conn.execute("INSERT INTO sales (product, amount, sold_at) VALUES ($1, $2, $3)", "Phone", 800.0, date(2024, 1, 15))
    await conn.execute("INSERT INTO sales (product, amount, sold_at) VALUES ($1, $2, $3)", "Laptop", 1300.0, date(2024, 1, 20))
    await conn.execute("INSERT INTO sales (product, amount, sold_at) VALUES ($1, $2, $3)", "Tablet", 500.0, date(2024, 1, 25))
    await conn.execute("INSERT INTO sales (product, amount, sold_at) VALUES ($1, $2, $3)", "Phone", 850.0, date(2024, 1, 30))
    materialized_view_sales_summary = """
    CREATE MATERIALIZED VIEW sales_summary AS
    SELECT product, SUM(amount) as total, COUNT(*) as count FROM sales GROUP BY product"""
    await conn.execute(materialized_view_sales_summary)
    fetch = await conn.fetch("SELECT * FROM sales_summary")
    print("Sales summary:", fetch)
    await conn.execute("INSERT INTO sales (product, amount, sold_at) VALUES ($1, $2, $3)", "Laptop", 1250.0, date(2024, 2, 5))
    refresh = "REFRESH MATERIALIZED VIEW sales_summary"
    await conn.execute(refresh)
    fetch_updated = await conn.fetch("SELECT * FROM sales_summary")
    print("Updated sales summary:", fetch_updated)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())