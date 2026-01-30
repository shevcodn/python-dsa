class Database:
	_isinstance = None

	def __new__(cls):
		if cls._isinstance is None:
			cls._isinstance = super().__new__(cls)
		return cls._isinstance

	def connect(self):
		return "Connected"

db1 = Database()
db2 = Database()

print(db1 is db2)
print(db1.connect())
