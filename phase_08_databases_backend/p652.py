import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        owner TEXT NOT NULL,
        balance REAL DEFAULT 0.0
    )
""")

cursor.execute("INSERT INTO users (owner, balance) VALUES (?, ?)", ("Denis", 1000.0))
cursor.execute("INSERT INTO users (owner, balance) VALUES (?, ?)", ("Sasha", 500.0))
conn.commit()

cursor.execute("SELECT * FROM users WHERE balance > ?", (300,))
print(cursor.fetchall())

cursor.execute("UPDATE users SET balance = balance + ? WHERE owner = ?", (500, "Denis"))
conn.commit()

cursor.execute("DELETE FROM users WHERE owner = ?", ("Sasha",))
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
