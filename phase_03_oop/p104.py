class SafeAccount:
	def __init__(self, balance):
		self.balance = balance

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance = self.balance - amount

	def get_balance(self):
		return self.balance

acc = SafeAccount(100)
acc.withdraw(30)
print(acc.get_balance())
acc.withdraw(200)
print(acc.get_balance())
