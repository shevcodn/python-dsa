import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        balance REAL DEFAULT 0.0
    )
""")

cursor.execute("INSERT INTO users (name, email, balance) VALUES (?, ?, ?)", ("Denis", "denis@test.com", 1000.0))
cursor.execute("INSERT INTO users (name, email, balance) VALUES (?, ?, ?)", ("Alice", "alice@test.com", 250.0))
cursor.execute("INSERT INTO users (name, email, balance) VALUES (?, ?, ?)", ("Bob", "bob@test.com", 50.0))
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()