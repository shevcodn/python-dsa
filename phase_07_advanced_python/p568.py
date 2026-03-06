import asyncio

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    async def __aenter__(self):
        print(f"Connecting to database {self.db_name}...")
        await asyncio.sleep(0.5)
        print("Connected!")
        return self
    
    async def __aexit__(self, *args):
        print("Closing connection...")
        await asyncio.sleep(0.2)
        print("Connection closed")

    async def main():
        async with DatabaseConnection("usets_db") as db:
            print(f"Running query on {db.db_name}...")


if __name__ == "__main__":
    asyncio.run(DatabaseConnection.main())