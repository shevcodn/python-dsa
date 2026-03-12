import os
import psycopg2

conn = psycopg2.connect(
    host="localhost", port=5432,
    database="learning", user="denis", password=os.getenv("DB_PASS", "password")
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        balance REAL DEFAULT 0.0)
""")
conn.commit()

cursor.execute("INSERT INTO users (name, email, balance) VALUES (%s, %s, %s)", ("Denis", "denis@example.com", 500.0))
cursor.execute("INSERT INTO users (name, email, balance) VALUES (%s, %s, %s)", ("Alice", "alice@example.com", 200.0))
cursor.execute("INSERT INTO users (name, email, balance) VALUES (%s, %s, %s)", ("Sonya", "sonya@example.com", 150.0))
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.close(), conn.close()