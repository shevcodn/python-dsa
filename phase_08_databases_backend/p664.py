import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT NOT NULL,
        balance REAL DEFAULT 0.0
    )
""")

cursor.execute("INSERT INTO accounts (owner, balance) VALUES (?, ?)", ("Denis", 1000.0))
cursor.execute("INSERT INTO accounts (owner, balance) VALUES (?, ?)", ("Alice", 500.0))
conn.commit()

print("=== SAVEPOINT DEMO ===")
cursor.execute("SELECT owner, balance FROM accounts")
print("Before:", cursor.fetchall())

cursor.execute("SAVEPOINT sp1")
cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE owner = 'Denis'")
cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE owner = 'Alice'")

cursor.execute("SELECT owner, balance FROM accounts")
print("After transfer (not committed):", cursor.fetchall())

cursor.execute("ROLLBACK TO sp1")
cursor.execute("SELECT owner, balance FROM accounts")
print("After rollback to savepoint:", cursor.fetchall())

cursor.execute("SAVEPOINT sp2")
cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE owner = 'Denis'")
cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE owner = 'Alice'")
cursor.execute("RELEASE sp2")
conn.commit()

cursor.execute("SELECT owner, balance FROM accounts")
print("After commit:", cursor.fetchall())

conn.close()
