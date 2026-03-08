import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        salesperson TEXT NOT NULL,
        region TEXT NOT NULL,
        amount REAL NOT NULL
    )
""")

data = [
    ("Denis", "North", 5000.0),
    ("Denis", "North", 3200.0),
    ("Denis", "South", 4100.0),
    ("Alice", "North", 6200.0),
    ("Alice", "South", 2800.0),
    ("Bob", "South", 7500.0),
    ("Bob", "East", 1900.0),
    ("Bob", "East", 3300.0),
]
cursor.executemany("INSERT INTO sales (salesperson, region, amount) VALUES (?, ?, ?)", data)
conn.commit()

print("=== WINDOW: ROW_NUMBER ===")
cursor.execute("""
    SELECT salesperson, amount,
           ROW_NUMBER() OVER (PARTITION BY salesperson ORDER BY amount DESC) as rank_in_person
    FROM sales
""")
for row in cursor.fetchall():
    print(row)

print("\n=== WINDOW: RANK overall ===")
cursor.execute("""
    SELECT salesperson, amount,
           RANK() OVER (ORDER BY amount DESC) as overall_rank
    FROM sales
    ORDER BY overall_rank
""")
for row in cursor.fetchall():
    print(row)

print("\n=== WINDOW: running total per person ===")
cursor.execute("""
    SELECT salesperson, amount,
           SUM(amount) OVER (PARTITION BY salesperson ORDER BY id) as running_total
    FROM sales
""")
for row in cursor.fetchall():
    print(row)

conn.close()
