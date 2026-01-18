class Wallet:
	def __init__(self):
		self.balance = 0


	def deposit(self, amount):
		self.balance = self.balance + amount


	def withdraw(self, amount):
		if amount > self.balance:
			return False
		self.balance = self.balance - amount
		return True

	def get_balance(self):
		return f"Available Balance: {self.balance}"

w = Wallet()
print(w.get_balance())

w.deposit(100)
print(w.get_balance())

print(w.withdraw(30))
print(w.get_balance())

print(w.withdraw(200))
print(w.get_balance())
