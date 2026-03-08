import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

data = [
    ("Denis", 500.0, "completed"),
    ("Denis", 200.0, "pending"),
    ("Alice", 1000.0, "completed"),
    ("Alice", 300.0, "failed"),
    ("Bob", 150.0, "completed"),
    ("Bob", 800.0, "completed"),
]
cursor.executemany("INSERT INTO transactions (customer, amount, status) VALUES (?, ?, ?)", data)
conn.commit()

cursor.execute("""
    CREATE VIEW completed_transactions AS
    SELECT customer, amount, created_at
    FROM transactions
    WHERE status = 'completed'
""")

cursor.execute("""
    CREATE VIEW customer_summary AS
    SELECT customer, COUNT(*) as total_orders, SUM(amount) as total_spent
    FROM transactions
    WHERE status = 'completed'
    GROUP BY customer
""")

print("=== VIEW: completed_transactions ===")
cursor.execute("SELECT * FROM completed_transactions")
for row in cursor.fetchall():
    print(row)

print("\n=== VIEW: customer_summary ===")
cursor.execute("SELECT * FROM customer_summary ORDER BY total_spent DESC")
for row in cursor.fetchall():
    print(row)

print("\n=== FILTER VIEW ===")
cursor.execute("SELECT * FROM customer_summary WHERE total_spent > 500")
for row in cursor.fetchall():
    print(row)

conn.close()
