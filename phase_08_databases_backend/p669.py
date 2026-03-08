import sqlite3
import csv
import io

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

data = [
    ("Denis", 500.0, "completed"),
    ("Denis", 200.0, "pending"),
    ("Alice", 1000.0, "completed"),
    ("Alice", 300.0, "failed"),
    ("Bob", 150.0, "completed"),
]
cursor.executemany("INSERT INTO transactions (customer, amount, status) VALUES (?, ?, ?)", data)
conn.commit()

print("=== EXPORT TO CSV (in-memory) ===")
cursor.execute("SELECT * FROM transactions")
rows = cursor.fetchall()
headers = [desc[0] for desc in cursor.description]

output = io.StringIO()
writer = csv.writer(output)
writer.writerow(headers)
writer.writerows(rows)
csv_content = output.getvalue()
print(csv_content)

print("=== IMPORT FROM CSV ===")
reader = csv.DictReader(io.StringIO(csv_content))
imported = []
for row in reader:
    imported.append((row["customer"], float(row["amount"]), row["status"]))

conn2 = sqlite3.connect(":memory:")
cursor2 = conn2.cursor()
cursor2.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT,
        amount REAL,
        status TEXT,
        created_at TEXT
    )
""")
for row in csv.DictReader(io.StringIO(csv_content)):
    cursor2.execute(
        "INSERT INTO transactions (id, customer, amount, status, created_at) VALUES (?, ?, ?, ?, ?)",
        (row["id"], row["customer"], row["amount"], row["status"], row["created_at"])
    )
conn2.commit()

cursor2.execute("SELECT customer, amount, status FROM transactions")
print("Imported rows:")
for row in cursor2.fetchall():
    print(row)

conn.close()
conn2.close()
