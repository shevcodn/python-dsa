import psycopg2

conn = psycopg2.connect(
    host="localhost", port=5432,
    database="learning", user="denis", password="denis777"
)
cursor = conn.cursor()

cursor.execute("""
    DROP TABLE IF EXISTS users
""")
conn.commit()

cursor.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        balance REAL DEFAULT 0.0)
""")
conn.commit()

cursor.execute("INSERT INTO users (balance) VALUES (%s)", (500.0,))
cursor.execute("INSERT INTO users (balance) VALUES (%s)", (200.0,))
cursor.execute("INSERT INTO users (balance) VALUES (%s)", (150.0,))
conn.commit()

cursor.execute("SELECT * FROM users WHERE balance > 200.0")
print(cursor.fetchall())

cursor.execute("UPDATE users SET balance = balance + 100.0 WHERE id = %s", (1,))
conn.commit()

cursor.execute("DELETE FROM users WHERE id = %s", (3,))

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.commit()
cursor.close()
conn.close()