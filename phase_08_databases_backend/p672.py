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

def insert_data(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("INSERT INTO {} (owner, balance) VALUES (%s, %s)").format(sql.Identifier("users")), ("Denis", 500.0))
        cursor.execute(sql.SQL("INSERT INTO {} (owner, balance) VALUES (%s, %s)").format(sql.Identifier("users")), ("Alice", 200.0))
        cursor.execute(sql.SQL("INSERT INTO {} (owner, balance) VALUES (%s, %s)").format(sql.Identifier("users")), ("Sonya", 150.0))
        conn.commit()

def select_data(conn):
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier("users")))
        print(cursor.fetchall())

if __name__ == "__main__":
    with get_connection() as conn:
        drop_table(conn)
        create_table(conn)
        insert_data(conn)
        select_data(conn)

