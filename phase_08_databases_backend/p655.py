import sqlite3

class Database:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                balance REAL DEFAULT 0.0
            )
        """)
        self.conn.commit()

    def add_account(self, owner: str, balance: float) -> None:
        self.cursor.execute("INSERT INTO users (name, email, balance) VALUES (?, ?, ?)", (owner, f"{owner.lower()}@test.com", balance))
        self.conn.commit()

    def get_account(self, owner: str) -> tuple:
        self.cursor.execute("SELECT * FROM users WHERE name = ?", (owner,))
        return self.cursor.fetchone()
    
    def update_balance(self, owner: str, amount: float) -> None:
        self.cursor.execute("UPDATE users SET balance = balance + ? WHERE name = ?", (amount, owner))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

print("=== DATABASE ===")
db = Database(":memory:")
db.add_account("Denis", 500.0)
db.add_account("Alice", 650.0)
print(db.get_account("Denis"))
db.update_balance("Denis", 200.0)
print(db.get_account("Denis"))
db.close()

