import os
import psycopg2
from psycopg2 import sql
from contextlib import contextmanager


@contextmanager
def get_connection():
    conn = psycopg2.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )
    try:
        yield conn
    finally:
        conn.close()

def drop_table(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier("users")))
        conn.commit()

def create_table(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("""
            CREATE TABLE IF NOT EXISTS {} (
                id SERIAL PRIMARY KEY,
                owner TEXT NOT NULL,
                balance real)
        """).format(sql.Identifier("users")))
        conn.commit()

def transfer(conn, from_id: int, to_id: int, amount: float) -> bool:
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT balance FROM {} WHERE id = %s").format(sql.Identifier("users")), (from_id,))
            from_balance = cursor.fetchone()[0]
            if from_balance < amount:
                raise ValueError("Insufficient funds")
            cursor.execute(sql.SQL("UPDATE {} SET balance = balance - %s WHERE id = %s").format(sql.Identifier("users")), (amount, from_id))
            cursor.execute(sql.SQL("UPDATE {} SET balance = balance + %s WHERE id = %s").format(sql.Identifier("users")), (amount, to_id))
            conn.commit()
            return True
    except Exception as e:
        conn.rollback()
        print(f"Transfer failed: {e}")
        return False
    


if __name__ == "__main__":
    with get_connection() as conn:
        drop_table(conn)
        create_table(conn)
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (owner, balance) VALUES (%s, %s)", ("Denis", 1000.0))
            cursor.execute("INSERT INTO users (owner, balance) VALUES (%s, %s)", ("Alice", 500.0))
            conn.commit()

        print("Transfer 300:", transfer(conn, 1, 2, 300))
        print("Transfer 5000:", transfer(conn, 1, 2, 5000))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            print(cursor.fetchall())