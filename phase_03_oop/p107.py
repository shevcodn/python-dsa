class ShoppingCart:
	def __init__(self):
		self.items = []

	def add_item(self, item):
		self.items.append(item)

	def get_items(self):
		return self.items

	def clear(self):
		self.items = []
	pass

cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Bread")
print(cart.get_items())
cart.clear()
print(cart.get_items())
