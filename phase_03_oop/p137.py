class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __repr__(self):
		return f"Product('{self.name}', {self.price})"


item = Product("Phone", 999)
print(repr(item))
