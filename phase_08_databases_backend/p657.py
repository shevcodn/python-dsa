import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY ,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO transactions (name, price, category) VALUES (?, ?, ?)", ("Iphone 15", 999.0, "electronics"))
cursor.execute("INSERT INTO transactions (name, price, category) VALUES (?, ?, ?)", ("MacBook Pro", 2499.0, "electronics"))
cursor.execute("INSERT INTO transactions (name, price, category) VALUES (?, ?, ?)", ("Nike Shoes", 20.0, "clothing"))
cursor.execute("INSERT INTO transactions (name, price, category) VALUES (?, ?, ?)", ("Adidas Jacket", 180.0, "clothing"))
cursor.execute("INSERT INTO transactions (name, price, category) VALUES (?, ?, ?)", ("Coffee Maker", 20.0, "appliances"))
cursor.execute("INSERT INTO transactions (name, price, category) VALUES (?, ?, ?)", ("Blender", 45.0, "appliances"))

print("=== LIKE 'a' ===")
cursor.execute("SELECT * FROM transactions WHERE name LIKE '%a%'")
print(cursor.fetchall())

print("=== ITEMS IN 'electronics' and 'clothing' ===")
cursor.execute("SELECT * FROM transactions WHERE category IN ('electronics', 'clothing')")
print(cursor.fetchall())

print("=== WHERE price BETWEEN 100 and 500 ===")
cursor.execute("SELECT * FROM transactions WHERE price BETWEEN 100 and 500")
print(cursor.fetchall())

conn.close()


