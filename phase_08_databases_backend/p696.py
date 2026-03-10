import asyncio
import asyncpg

async def main():
    conn_listener = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )
    conn_sender = await asyncpg.connect(
        host="localhost", port=5432,
        database="learning", user="denis", password="denis777"
    )

    await conn_sender.execute("DROP TABLE IF EXISTS events CASCADE")
    await conn_sender.execute("CREATE TABLE events (id SERIAL PRIMARY KEY, message TEXT NOT NULL, created_at TIMESTAMP DEFAULT NOW())")

    def callback(conn, pid, channel, payload):
        print(f"Received: {payload}")

    await conn_listener.add_listener("new_event", callback)

    await conn_sender.execute("INSERT INTO events (message) VALUES ($1)", "Hello from sender!")
    await conn_sender.execute("NOTIFY new_event, 'Hello from sender!'")

    await asyncio.sleep(0.5)

    await conn_listener.close()
    await conn_sender.close()

if __name__ == "__main__":
    asyncio.run(main())
