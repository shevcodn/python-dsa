class Database:
    def query(self, sql):
        print(f"Executing: {sql}")

class DataBaseProxy:
    def __init__(self):
        self.database = Database()

    def query(self, sql, user):
        if user == "admin":
            self.database.query(sql)
        else:
            print("Access denied")

db = DataBaseProxy()

db.query("SELECT * FROM users", user="admin")
db.query("DELETE FROM users", user="guest")