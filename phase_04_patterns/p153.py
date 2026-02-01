class BankAccount:
	def __init__(self, balance):
		self._balance = balance

	@property
	def balance(self):
		return self._balance

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("Amount must be positive")
		self._balance += amount

	def withdraw(self, amount):
		if amount <= 0:
			raise ValueError("Amount must be positive")
		if amount > self._balance:
			raise ValueError("Insufficient funds")
		self._balance -= amount

acc = BankAccount(100)
print(acc.balance)

acc.deposit(50)
print(acc.balance)

acc.withdraw(30)
print(acc.balance)

acc.withdraw(200)
