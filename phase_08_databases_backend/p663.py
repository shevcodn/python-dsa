import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
""")

cursor.executemany("INSERT INTO customers (name, city) VALUES (?, ?)", [
    ("Denis", "Toronto"),
    ("Alice", "Vancouver"),
    ("Bob", "Montreal"),
])
cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", [
    ("Laptop", 1200.0),
    ("Mouse", 50.0),
    ("Monitor", 400.0),
])
cursor.executemany("INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)", [
    (1, 1, 1),
    (1, 2, 2),
    (2, 3, 1),
    (3, 2, 3),
])
conn.commit()

print("=== 3-TABLE JOIN ===")
cursor.execute("""
    SELECT c.name, p.name, o.quantity, (p.price * o.quantity) as total
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN products p ON o.product_id = p.id
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n=== CUSTOMER TOTALS ===")
cursor.execute("""
    SELECT c.name, c.city, SUM(p.price * o.quantity) as spent
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN products p ON o.product_id = p.id
    GROUP BY c.id
    ORDER BY spent DESC
""")
for row in cursor.fetchall():
    print(row)

conn.close()
