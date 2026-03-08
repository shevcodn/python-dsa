import random
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")
random.seed(42)
statuses = ["completed", "pending", "failed"]
data = [(random.randint(1, 10), round(random.uniform(10, 2000), 2), random.choice(statuses)) for _ in range(50)]
cursor.executemany("INSERT INTO transactions (user_id, amount, status) VALUES (?, ?, ?)", data)
conn.commit()

cursor.execute("CREATE INDEX idx_user_id ON transactions(user_id)")
cursor.execute("CREATE INDEX idx_status ON transactions(status)")
cursor.execute("CREATE INDEX idx_user_status ON transactions(user_id, status)")

print("=== QUERY WITH INDEX ===")
cursor.execute("SELECT * FROM transactions WHERE user_id = 3 AND status = 'completed'")
rows = cursor.fetchall()
print(f"User 3 completed: {len(rows)} transactions")
for row in rows:
    print(row)

print("\n=== INDEX INFO ===")
cursor.execute("SELECT name, tbl_name FROM sqlite_master WHERE type = 'index'")
for row in cursor.fetchall():
    print(row)

conn.close()
