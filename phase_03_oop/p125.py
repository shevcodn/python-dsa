class Account:
	def __init__(self, name):
		self.name = name
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount

	def get_balance(self):
		return self.balance


class Bank:
	def __init__(self):
		self.accounts = {}

	def create_account(self, name):
		new_account = Account(name)
		self.accounts[name] = new_account

	def get_account(self, name):
		return self.accounts[name]


	def total_money(self):
		total = 0
		for account in self.accounts.values():
			total += account.get_balance()
		return total

bank = Bank()
bank.create_account("Denis")
bank.create_account("Pasha")

bank.get_account("Denis").deposit(1000)
bank.get_account("Pasha").deposit(500)

print(bank.total_money())

bank.get_account("Denis").withdraw(200)
print(bank.get_account("Denis").get_balance())
