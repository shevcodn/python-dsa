class DataBaseConnection:
    _instance = None
    
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def connect(self):
        print("Connected to database")

    def disconnect(self):
        print("Disconnected from database")
    

db1 = DataBaseConnection()
db1.connect()

db2= DataBaseConnection()
db2.connect()

print(db1 is db2)
print(id(db1))
print(id(db2))