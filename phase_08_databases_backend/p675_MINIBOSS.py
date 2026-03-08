import psycopg2
from psycopg2 import sql
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )
    try:
        yield conn
    finally:
        conn.close()

class UserRepository:
    def __init__(self, conn):
        self.conn = conn
    
    def create(self, name, email, balance) -> int:
        with self.conn.cursor() as cursor:
            cursor.execute(sql.SQL("INSERT INTO {} (name, email, balance) VALUES (%s, %s, %s) RETURNING id").format(sql.Identifier("users")), (name, email, balance))
            user_id = cursor.fetchone()[0]
            self.conn.commit()
            return user_id
        
    def find_by_id(self, user_id) -> dict:
        with self.conn.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT * FROM {} WHERE id = %s").format(sql.Identifier("users")), (user_id,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "name": row[1], "email": row[2], "balance": row[3]}
            return None
        
    def find_by_email(self, email) -> dict:
        with self.conn.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT * FROM {} WHERE email = %s").format(sql.Identifier("users")), (email,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "name": row[1], "email": row[2], "balance": row[3]}
            return None
        
    def update_balance(self, user_id, new_balance) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute(sql.SQL("UPDATE {} SET balance = %s WHERE id = %s").format(sql.Identifier("users")), (new_balance, user_id))
            self.conn.commit()

    def delete(self, user_id) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute(sql.SQL("DELETE FROM {} WHERE id = %s").format(sql.Identifier("users")), (user_id,))
            self.conn.commit()

    def find_all(self) -> list:
        with self.conn.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier("users")))
            rows = cursor.fetchall()
            return [{"id": row[0], "name": row[1], "email": row[2], "balance": row[3]} for row in rows]
        
if __name__ == "__main__":
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users")
            cursor.execute("""
                CREATE TABLE users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    balance REAL DEFAULT 0.0
                )
            """)
            conn.commit()
        repo = UserRepository(conn)
        user_id = repo.create("Denis", "denis@example.com", 1000.0)
        print("Find by ID:", repo.find_by_id(user_id))
        print("Find by email:", repo.find_by_email("denis@example.com"))
        update_balance = repo.find_by_id(user_id)["balance"] + 500.0
        repo.update_balance(user_id, update_balance)
        print("After balance update:", repo.find_by_id(user_id))
        user_id = repo.create("Alice", "alice@example.com", 500.0)
        print("Find by ID:", repo.find_by_id(user_id))
        print("Find by email:", repo.find_by_email("alice@example.com"))
        update_balance = repo.find_by_email("alice@example.com")["balance"] - 200.0
        repo.update_balance(user_id, update_balance)
        print("After balance update:", repo.find_by_email("alice@example.com"))
        user_id = repo.create("Sonya", "sonya@example.com", 300.0)
        print("Find by ID:", repo.find_by_id(user_id))
        print("Find by email:", repo.find_by_email("sonya@example.com"))
        update_balance = repo.find_by_email("sonya@example.com")["balance"] + 100.0
        repo.update_balance(user_id, update_balance)
        print("After balance update:", repo.find_by_email("sonya@example.com"))
        delete_user_id = repo.find_by_email("sonya@example.com")["id"]
        repo.delete(delete_user_id)
        print("After deletion, find by email:", repo.find_by_email("sonya@example.com"))
        print("All users:", repo.find_all())
        

