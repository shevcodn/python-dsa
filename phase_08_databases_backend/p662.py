import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT NOT NULL,
        product TEXT NOT NULL,
        amount REAL NOT NULL
    )
""")

data = [
    ("Denis", "laptop", 1200.0),
    ("Denis", "mouse", 50.0),
    ("Denis", "keyboard", 100.0),
    ("Alice", "monitor", 400.0),
    ("Alice", "headset", 80.0),
    ("Bob", "webcam", 60.0),
]
cursor.executemany("INSERT INTO orders (customer, product, amount) VALUES (?, ?, ?)", data)
conn.commit()

print("=== GROUP BY customer ===")
cursor.execute("SELECT customer, COUNT(*) as orders, SUM(amount) as total FROM orders GROUP BY customer")
for row in cursor.fetchall():
    print(row)

print("\n=== HAVING total > 200 ===")
cursor.execute("""
    SELECT customer, SUM(amount) as total
    FROM orders
    GROUP BY customer
    HAVING total > 200
""")
for row in cursor.fetchall():
    print(row)

print("\n=== HAVING COUNT > 1 ===")
cursor.execute("""
    SELECT customer, COUNT(*) as num_orders
    FROM orders
    GROUP BY customer
    HAVING num_orders > 1
    ORDER BY num_orders DESC
""")
for row in cursor.fetchall():
    print(row)

conn.close()
