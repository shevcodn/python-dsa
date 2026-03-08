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

def drop_table(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier("users")))
        conn.commit()

def create_table(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("""
                CREATE TABLE IF NOT EXISTS {} (
                id SERIAL PRIMARY KEY,
                customer TEXT NOT NULL,
                amount REAL NOT NULL,
                status TEXT NOT NULL
        )""").format(sql.Identifier("users")))
        conn.commit()

def executemany(conn):
    with conn.cursor() as cursor:
        data = [
            ("Denis", 100.0, "completed"),
            ("Alice", 200.0, "pending"),
            ("Sonya", 150.0, "completed"),
            ("Sasha", 300.0, "pending")
        ]

        cursor.executemany(sql.SQL("INSERT INTO {} (customer, amount, status) VALUES (%s, %s, %s)").format(sql.Identifier("users")), data)
        conn.commit()
        print(f"Inserted {cursor.rowcount} rows")

def print_inserted_rows(cursor):
    print(f"Inserted {cursor.rowcount} rows")

def fetchall(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier("users")))
        print(cursor.fetchall())

def fetchone(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier("users")))
        print(cursor.fetchone())

def cursor_execute(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("SELECT * FROM {} WHERE status = %s").format(sql.Identifier("users")), ("completed",))
        print(cursor.fetchall())

if __name__ == "__main__":
    with get_connection() as conn:
        drop_table(conn)
        create_table(conn)
        executemany(conn)
        fetchall(conn)
        fetchone(conn)
        cursor_execute(conn)
