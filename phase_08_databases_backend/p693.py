import asyncio
import asyncpg
from datetime import date

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )

    await conn.execute("DROP TABLE IF EXISTS transactions_2023")
    await conn.execute("DROP TABLE IF EXISTS transactions_2024")
    await conn.execute("DROP TABLE IF EXISTS transactions CASCADE")

    await conn.execute("""
        CREATE TABLE transactions (
            id SERIAL,
            amount REAL NOT NULL,
            created_at DATE NOT NULL
        ) PARTITION BY RANGE (created_at)
    """)

    await conn.execute("""
        CREATE TABLE transactions_2023 PARTITION OF transactions
        FOR VALUES FROM ('2023-01-01') TO ('2024-01-01')
    """)

    await conn.execute("""
        CREATE TABLE transactions_2024 PARTITION OF transactions
        FOR VALUES FROM ('2024-01-01') TO ('2025-01-01')
    """)

    await conn.execute("INSERT INTO transactions (amount, created_at) VALUES ($1, $2)", 100.0, date(2023, 1, 15))
    await conn.execute("INSERT INTO transactions (amount, created_at) VALUES ($1, $2)", 200.0, date(2023, 6, 20))
    await conn.execute("INSERT INTO transactions (amount, created_at) VALUES ($1, $2)", 300.0, date(2024, 2, 10))
    await conn.execute("INSERT INTO transactions (amount, created_at) VALUES ($1, $2)", 400.0, date(2024, 11, 5))

    all_rows = await conn.fetch("SELECT * FROM transactions ORDER BY created_at")
    print("All transactions:", all_rows)

    rows_2023 = await conn.fetch("SELECT * FROM transactions_2023 ORDER BY created_at")
    print("2023 transactions:", rows_2023)

    rows_2024 = await conn.fetch("SELECT * FROM transactions_2024 ORDER BY created_at")
    print("2024 transactions:", rows_2024)

    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
