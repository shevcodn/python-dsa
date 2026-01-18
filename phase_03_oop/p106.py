class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def is_expensive(self):
		if self.price > 100:
			return True
		else:
			return False

	def apply_discount(self, percent):
		self.price = self.price - (self.price * percent / 100)

p1 = Product("Phone", 200)
p2 = Product("Book", 15)

print(p1.is_expensive())
print(p2.is_expensive())

p1.apply_discount(25)
print(p1.price) 
