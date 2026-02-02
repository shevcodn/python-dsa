class Product:
	def __init__(self, name, price):
		self._name = name
		self._price = price
		self._discount = 0

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, value):
		if value < 0:
			raise ValueError("Price cannot be negative")
		self._price = value


	@property
	def discount(self):
		return self._discount

	@discount.setter
	def discount(self, value):
		if value < 0 or value > 100:
			raise ValueError("Discount must be 0-100")
		self._discount = value

	@property
	def final_price(self):
		return self._price - (self._price * self._discount / 100)


p = Product("Laptop", 1000)
print(p.price)
print(p.final_price)

p.discount = 20
print(p.final_price)

p.discount = 150
