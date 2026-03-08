class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        self.connected = True
        print(f"Connected to {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        print(f"Disconnected from {self.db_name}")
        return False


class Timer:
    def __init__(self, label: str):
        self.label = label
        self.start = None

    def __enter__(self):
        import time
        self.start = time.time()
        print(f"[{self.label}] started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"[{self.label}] done in {elapsed:.3f}s")
        return False


with DatabaseConnection("payments_db") as db:
    print(f"Is connected: {db.connected}")

with Timer("query"):
    total = sum(range(1000000))
    print(f"Sum: {total}")
