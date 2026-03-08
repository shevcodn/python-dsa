import sqlite3

class UserRepository:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE transactions (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email UNIQUE NOT NULL,
                balance REAL DEFAULT 0.0
            )
        """)

    def create(self, name: str, email: str, balance: float = 0.0) -> int:
        self.cursor.execute("INSERT INTO transactions (name, email, balance) VALUES (?, ?, ?)", (name, email, balance))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def find_by_id(self, user_id: int) -> dict:
        self.cursor.execute("SELECT * FROM transactions WHERE id = ?", (user_id,))
        row = self.cursor.fetchone()
        return {"id": row[0], "name": row[1], "email": row[2], "balance": row[3]} if row else None
    
    def find_by_email(self, email: str) -> dict:
        self.cursor.execute("SELECT * FROM transactions WHERE email = ?", (email,))
        row = self.cursor.fetchone()
        return {"id": row[0], "name": row[1], "email": row[2], "balance": row[3]} if row else None

    def update_balance(self, user_id: int, amount: float) -> None:
        self.cursor.execute("UPDATE transactions SET balance = balance + ? WHERE id =?", (amount, user_id))
        self.conn.commit()

    def delete(self, user_id: int) -> None:
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (user_id,))
        self.conn.commit()

    def find_all(self) -> list:
        self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()

conn = sqlite3.connect(":memory:")
repo = UserRepository(conn)

repo.create("Denis", "denis@example.com", 1000.0)
repo.create("Alice", "alice@example.com", 500.0)
repo.create("Sasha", "sasha@example.com", 250.0)

print(repo.find_by_id(1))
print(repo.find_by_email("alice@example.com"))

repo.update_balance(1, 200.0)
print(repo.find_by_id(1))

repo.delete(3)
print(repo.find_all())


