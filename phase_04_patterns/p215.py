class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance        

    def __init__(self):
        pass

    def connect(self):
        print("Connected to database")

db1 = Database()
db2 = Database()

print(db1 is db2)
db1.connect()