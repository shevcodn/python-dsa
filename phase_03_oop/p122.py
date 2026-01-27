class Calculator:
	def __init__(self):
		self.memory = 0

	def add(self, n):
		self.memory += n

	def subtract(self, n):
		self.memory -= n

	def multiply(self, n):
		self.memory *= n

	def get_results(self):
		return self.memory


calc = Calculator()
calc.add(10)
calc.subtract(3)
calc.multiply(2)
print(calc.get_results())
