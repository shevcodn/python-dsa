import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )

    await conn.execute("DROP TABLE IF EXISTS employees")
    await conn.execute("CREATE TABLE IF NOT EXISTS employees (id SERIAL PRIMARY KEY, name TEXT NOT NULL, manager_id INT)")
    await conn.execute("INSERT INTO employees (name, manager_id) VALUES ($1, $2)", "Denis", None)
    await conn.execute("INSERT INTO employees (name, manager_id) VALUES ($1, $2)", "Alice", 1)
    rows = await conn.fetch("SELECT * FROM employees")
    print("All employees:", rows)
    await conn.execute("INSERT INTO employees (name, manager_id) VALUES ($1, $2)", "Bob", 1)
    await conn.execute("INSERT INTO employees (name, manager_id) VALUES ($1, $2)", "Carol", 2)
    rows = await conn.fetch("SELECT e1.id, e1.name, e2.name as manager_name FROM employees e1 LEFT JOIN employees e2 ON e1.manager_id = e2.id")
    print("All employees with managers:", rows)
    recursive_cte = await conn.fetch("""
        WITH RECURSIVE hierarchy AS (
            SELECT id, name, manager_id, 0 AS level
            FROM employees WHERE manager_id IS NULL
            UNION ALL
            SELECT e.id, e.name, e.manager_id, h.level + 1
            FROM employees e JOIN hierarchy h ON e.manager_id = h.id
        )
        SELECT * FROM hierarchy ORDER BY level
    """)
    print("Employee hierarchy:", recursive_cte)

    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())