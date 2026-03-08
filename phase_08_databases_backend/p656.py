import sqlite3


class BankDB:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner TEXT NOT NULL,
                balance REAL DEFAULT 0.0
            )
        """)
        self.conn.commit()

    def add_account(self, owner, balance: float) -> None:
        self.cursor.execute("INSERT INTO users (owner, balance) VALUES (?, ?)", (owner, balance))
        self.conn.commit()

    def transfer(self, from_owner, to_owner, amount: float) -> None:
        try:
            balance = self.get_balance(from_owner)
            if balance < amount:
                raise ValueError("Insufficient funds")
            self.cursor.execute("UPDATE users SET balance = balance - ? WHERE owner = ?", (amount, from_owner))
            self.cursor.execute("UPDATE users SET balance = balance + ? WHERE owner = ?", (amount, to_owner))
            self.conn.commit()
            print(f"Transfer successful: {amount}")
        except Exception as e:
            self.conn.rollback()
            print(f"Transfer failed, rolled back: {e}")

    def get_balance(self, owner) -> float:
        self.cursor.execute("SELECT balance FROM users WHERE owner = ?", (owner,))
        result = self.cursor.fetchone()
        return result[0] if result else 0.0

    def close(self):
        self.conn.close()


db = BankDB(":memory:")
db.add_account("Denis", 1000.0)
db.add_account("Alice", 500.0)

print(f"Denis: {db.get_balance('Denis')}, Alice: {db.get_balance('Alice')}")
db.transfer("Denis", "Alice", 300.0)
print(f"Denis: {db.get_balance('Denis')}, Alice: {db.get_balance('Alice')}")

db.transfer("Denis", "Alice", 2000.0)
print(f"Denis: {db.get_balance('Denis')}, Alice: {db.get_balance('Alice')}")

db.close()
