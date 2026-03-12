import os
import asyncio
import asyncpg
import time

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )

    await conn.execute("DROP TABLE IF EXISTS products CASCADE")
    await conn.execute("CREATE TABLE IF NOT EXISTS products (id SERIAL PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL, updated_at TIMESTAMP DEFAULT NOW())")

    await conn.execute("""
        CREATE OR REPLACE FUNCTION update_timestamp()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """)
    await conn.execute("""
        CREATE TRIGGER set_timestamp
        BEFORE UPDATE ON products
        FOR EACH ROW
        EXECUTE FUNCTION update_timestamp();
    """)
    await conn.execute("INSERT INTO products (name, price) VALUES ($1, $2)", "Laptop", 1200.0)
    fetchrow = await conn.fetchrow("SELECT * FROM products WHERE id = $1", 1)
    print("Before update:", fetchrow)
    await asyncio.sleep(1)
    await conn.execute("UPDATE products SET price = $1 WHERE id = $2", 1300.0, 1)
    fetchrow = await conn.fetchrow("SELECT * FROM products WHERE id = $1", 1)
    print("After update:", fetchrow["updated_at"])
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
        