import os
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )

    await conn.execute("DROP TABLE IF EXISTS articles")
    await conn.execute("CREATE TABLE articles (id SERIAL PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL, search_vector tsvector)")
    await conn.execute("INSERT INTO articles (title, body) VALUES ($1, $2)", "Introduction to Asyncio", "Asyncio is a powerful library for writing concurrent code in Python. It allows you to write asynchronous code using the async/await syntax.")
    await conn.execute("INSERT INTO articles (title, body) VALUES ($1, $2)", "Getting Started with Asyncpg", "Asyncpg is a fast PostgreSQL client library for Python. It provides an easy-to-use interface for interacting with PostgreSQL databases asynchronously.")
    await conn.execute("INSERT INTO articles (title, body) VALUES ($1, $2)", "Advanced Asyncio Patterns", "In this article, we will explore some advanced patterns for using asyncio, including task groups, cancellation, and error handling.")
    update = await conn.execute("UPDATE articles SET search_vector = to_tsvector('english', title || ' ' || body)")
    print("Update result:", update)
    search = await conn.fetch("SELECT * FROM articles WHERE search_vector @@ to_tsquery('english', $1)", "asyncio")
    print("Search results for 'asyncio':", search)
    search = await conn.fetch("""
        SELECT *, ts_rank(search_vector, to_tsquery('english', 'asyncpg')) as rank
        FROM articles
        WHERE search_vector @@ to_tsquery('english', 'asyncpg')
        ORDER BY rank DESC
    """)
    print("Search results with rank:", search)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())