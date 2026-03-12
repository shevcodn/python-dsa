import os
import asyncio
import asyncpg

async def main():
    conn1 = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )
    conn2 = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )

    lock1 = await conn1.fetchval("SELECT pg_try_advisory_lock(12345)")
    print("Lock acquired by conn1:", lock1)

    lock2 = await conn2.fetchval("SELECT pg_try_advisory_lock(12345)")
    print("Lock acquired by conn2 (should be False):", lock2)

    released = await conn1.fetchval("SELECT pg_advisory_unlock(12345)")
    print("Lock released by conn1:", released)

    lock2_retry = await conn2.fetchval("SELECT pg_try_advisory_lock(12345)")
    print("Lock acquired by conn2 after release:", lock2_retry)

    await conn1.close()
    await conn2.close()

if __name__ == "__main__":
    asyncio.run(main())     