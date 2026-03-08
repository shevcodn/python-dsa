import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Denis", "denis@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
conn.commit()

cursor.execute("ALTER TABLE users ADD COLUMN phone TEXT DEFAULT 'unknown'")
cursor.execute("ALTER TABLE users ADD COLUMN verified INTEGER DEFAULT 0")
conn.commit()

cursor.execute("UPDATE users SET phone = '+1-416-555-0001', verified = 1 WHERE name = 'Denis'")
cursor.execute("UPDATE users SET phone = '+1-416-555-0002', verified = 1 WHERE name = 'Alice'")
conn.commit()

print("=== AFTER MIGRATION ===")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

print("\n=== VERIFIED ONLY ===")
cursor.execute("SELECT name, phone FROM users WHERE verified = 1")
for row in cursor.fetchall():
    print(row)

conn.close()
