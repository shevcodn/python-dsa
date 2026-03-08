import sqlite3

class BankRepository:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner TEXT NOT NULL,
                balance REAL DEFAULT 0.0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_id INTEGER,
                to_id INTEGER,
                amount REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def create_account(self, owner, balance: float) -> int:
        self.cursor.execute("INSERT INTO accounts (owner, balance) VALUES (?, ?)", (owner, balance))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_account(self, account_id: int) -> dict:
        self.cursor.execute("SELECT * FROM accounts WHERE id = ?", (account_id,))
        row = self.cursor.fetchone()
        return {"id": row[0], "owner": row[1], "balance": row[2]} if row else None

    def transfer(self, from_id: int, to_id: int, amount: float) -> bool:
        try:
            self.cursor.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,))
            from_balance = self.cursor.fetchone()[0]
            if from_balance < amount:
                raise ValueError("Insufficient funds")
            self.cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))
            self.cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))
            self.cursor.execute("INSERT INTO transactions (from_id, to_id, amount) VALUES (?, ?, ?)", (from_id, to_id, amount))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Transfer failed: {e}")
            return False

    def get_history(self, account_id: int) -> list:
        self.cursor.execute("SELECT * FROM transactions WHERE from_id = ? OR to_id = ?", (account_id, account_id))
        return self.cursor.fetchall()
        
repo = BankRepository()
acc1 = repo.create_account("Denis", 1000.0)
acc2 = repo.create_account("Alice", 500.0)

print(repo.get_account(acc1))
print(repo.get_account(acc2))

repo.transfer(acc1, acc2, 300.0)
print(repo.get_account(acc1))
print(repo.get_account(acc2))

repo.transfer(acc1, acc2, 2000.0)
print(repo.get_account(acc1))
print(repo.get_account(acc2))

