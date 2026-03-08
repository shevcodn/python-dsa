import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO transactions (user_name, amount, category) VALUES (?, ?, ?)", ("Denis", 500.0, "food"))
cursor.execute("INSERT INTO transactions (user_name, amount, category) VALUES (?, ?, ?)", ("Denis", 200.0, "transport"))
cursor.execute("INSERT INTO transactions (user_name, amount, category) VALUES (?, ?, ?)", ("Victoria", 1000.0, "food"))
cursor.execute("INSERT INTO transactions (user_name, amount, category) VALUES (?, ?, ?)", ("Victoria", 300.0, "food"))
cursor.execute("INSERT INTO transactions (user_name, amount, category) VALUES (?, ?, ?)", ("Sasha", 150.0, "transport"))
cursor.execute("INSERT INTO transactions (user_name, amount, category) VALUES (?, ?, ?)", ("Sasha", 800.0, "food"))
conn.commit()


print("=== ORDER BY amount DESC ===")
cursor.execute("SELECT * FROM transactions ORDER BY amount DESC")
print(cursor.fetchall())


print("=== TOP 3 ===")
cursor.execute("SELECT * FROM transactions ORDER BY amount DESC LIMIT 3")
print(cursor.fetchall())


print("=== GROUP BY user ===")
cursor.execute("SELECT user_name, SUM(amount) FROM transactions GROUP BY user_name")
print(cursor.fetchall())

conn.close()
