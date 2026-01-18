class BankAccount:
	def __init__(self, balance):
		self.balance = balance

	def deposit(self, amount):
		self.balance = self.balance + amount

	def withdraw(self, amount):
		self.balance = self.balance - amount

	def get_balance(self):
		f"Balance: {self.balance}"
		return self.balance

acc = BankAccount(100)
print(acc.get_balance())
acc.deposit(50)
print(acc.get_balance())
acc.withdraw(30)
print(acc.get_balance())
