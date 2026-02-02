class BankAccount:
	def __init__(self, owner, balance):
		self._owner = owner
		self._balance = balance
		balance = 0

	@property
	def owner(self):
		return self._owner

	@property
	def balance(self):
		return self._balance

	@balance.setter
	def balance(self, value):
		if value < 0:
			raise ValueError("Balance cannot be negative")
		value = self._balance


	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("Amount must be positive")
		self._balance += amount


	def withdraw(self, amount):
		if amount <= 0:
			raise ValueError("Amount must be positive")
		elif amount > self._balance:
			raise ValueError("Insufficient funds")
		self._balance -= amount

	def __str__(self):
		return f"{self._owner}: ${self._balance}"

acc = BankAccount("Denis", 1000)
print(acc)

acc.deposit(500)
print(acc.balance)

acc.withdraw(200)
print(acc)
