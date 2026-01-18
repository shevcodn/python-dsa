class Inventory:
	def __init__(self):
		self.items = {}

	def add(self, item, qty):
		if item in self.items:
			self.items[item] = self.items[item] + qty
		else:
			self.items[item] = qty

	def get_qty(self, item):
		if item in self.items:
			return self.items[item]
		else:
			return 0

inv = Inventory()
inv.add("apple", 5)
inv.add("bread", 2)
inv.add("apple", 3)
print(inv.get_qty("apple"))
print(inv.get_qty("bread"))
print(inv.get_qty("milk"))
