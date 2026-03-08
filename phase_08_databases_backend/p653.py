import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE transactions (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL)")

cursor.execute("INSERT INTO users (name) VALUES (?)", ("Denis",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Victoria",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Sasha",))

cursor.execute("INSERT INTO transactions (user_id, amount) VALUES (?, ?)", (1, 200.0))
cursor.execute("INSERT INTO transactions (user_id, amount) VALUES (?, ?)", (2, 150.0))
cursor.execute("INSERT INTO transactions (user_id, amount) VALUES (?, ?)", (3, 300.0))
conn.commit()

cursor.execute("""
    SELECT users.name, transactions.amount
    FROM transactions
    JOIN users ON transactions.user_id = users.id
""")
print(cursor.fetchall())

conn.close()
