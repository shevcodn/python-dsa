import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    curstomer TEXT NOT NULL,
    amount REAL NOT NULL,
    status TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO transactions (curstomer, amount, status) VALUES (?, ?, ?)", ("Denis", 500.0, "completed"))
cursor.execute("INSERT INTO transactions (curstomer, amount, status) VALUES (?, ?, ?)", ("Denis", 200.0, "pending"))
cursor.execute("INSERT INTO transactions (curstomer, amount, status) VALUES (?, ?, ?)", ("Alice", 1000.0, "completed"))
cursor.execute("INSERT INTO transactions (curstomer, amount, status) VALUES (?, ?, ?)", ("Alice", 300.0, "completed"))
cursor.execute("INSERT INTO transactions (curstomer, amount, status) VALUES (?, ?, ?)", ("Bob", 150.0, "cancelled"))
cursor.execute("INSERT INTO transactions (curstomer, amount, status) VALUES (?, ?, ?)", ("Denis", 800.0, "completed"))
cursor.execute("INSERT INTO transactions (curstomer, amount, status) VALUES (?, ?, ?)", ("Denis", 350.0, "completed"))

print("=== AMOUNT COMPLETED ===")
cursor.execute("SELECT SUM(amount) FROM transactions WHERE status = 'completed'")
print(cursor.fetchone())

print("=== MEDIAN AMOUNT ===")
cursor.execute("SELECT amount FROM transactions WHERE status = 'completed' ORDER BY amount")
amount = [row[0] for row in cursor.fetchall()]
print(amount[len(amount) // 2] if len(amount) % 2 == 1 else (amount[len(amount) // 2 - 1] + amount[len(amount) // 2]) / 2)

print("=== SUBQUERY ===")
cursor.execute("SELECT curstomer, (SELECT SUM(amount) FROM transactions t2 WHERE t2.curstomer = t1.curstomer AND status = 'completed') AS total_completed FROM transactions t1 GROUP BY curstomer")
print(cursor.fetchall())

conn.close()
