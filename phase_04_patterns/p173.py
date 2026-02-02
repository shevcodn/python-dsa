class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __str__(self):
		return f"{self.name}: ${self.price}"

class ShoppingCart:
	def __init__(self):
		self.items = []

	def add_item(self, product):
		self.items.append(product)

	def get_total(self):
		total = 0
		for product in self.items:
			total += product.price
		return total

cart = ShoppingCart()

cart.add_item(Product("Laptop", 1000))
cart.add_item(Product("Mouse", 50))
cart.add_item(Product("Keyboard", 100))

print(cart.get_total())
