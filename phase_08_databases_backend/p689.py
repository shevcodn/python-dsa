import os
import asyncio
import asyncpg
import time



async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )

    await conn.execute("DROP TABLE IF EXISTS transactions")
    await conn.execute("CREATE TABLE IF NOT EXISTS transactions (id SERIAL PRIMARY KEY, user_id INT, amount REAL NOT NULL, status TEXT NOT NULL)")
    await conn.execute("INSERT INTO transactions (user_id, amount, status) VALUES ($1, $2, $3)", 1, 100.0, "pending")
    await conn.execute("INSERT INTO transactions (user_id, amount, status) VALUES ($1, $2, $3)", 1, 150.0, "pending")
    start = time.time()
    await conn.executemany("UPDATE transactions SET status = $1 WHERE user_id = $2", [("completed", 1), ("failed", 1)])
    end = time.time()
    print(f"Executed in {end - start:.4f} seconds")
    start = time.time()
    await conn.copy_records_to_table('transactions', records=[(1, 200.0, "pending"), (1, 250.0, "pending")], columns=['user_id', 'amount', 'status'])
    end = time.time()
    print(f"Copied in {end - start:.4f} seconds")
    
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())

