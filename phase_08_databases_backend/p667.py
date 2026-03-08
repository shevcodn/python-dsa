import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        status TEXT NOT NULL
    )
""")

data = [
    ("Denis", 500.0, "food", "completed"),
    ("Denis", 1200.0, "electronics", "completed"),
    ("Denis", 50.0, "transport", "pending"),
    ("Alice", 300.0, "food", "completed"),
    ("Alice", 800.0, "electronics", "failed"),
    ("Alice", 120.0, "clothing", "completed"),
    ("Bob", 75.0, "food", "completed"),
    ("Bob", 2000.0, "electronics", "completed"),
    ("Bob", 45.0, "transport", "completed"),
]
cursor.executemany("INSERT INTO transactions (customer, amount, category, status) VALUES (?, ?, ?, ?)", data)
conn.commit()

print("=== CTE: total per customer ===")
cursor.execute("""
    WITH customer_totals AS (
        SELECT customer, SUM(amount) as total
        FROM transactions
        WHERE status = 'completed'
        GROUP BY customer
    )
    SELECT * FROM customer_totals
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n=== CTE: above average spenders ===")
cursor.execute("""
    WITH customer_totals AS (
        SELECT customer, SUM(amount) as total
        FROM transactions
        WHERE status = 'completed'
        GROUP BY customer
    ),
    avg_spend AS (
        SELECT AVG(total) as avg_total FROM customer_totals
    )
    SELECT ct.customer, ct.total
    FROM customer_totals ct, avg_spend
    WHERE ct.total > avg_spend.avg_total
""")
for row in cursor.fetchall():
    print(row)

conn.close()
