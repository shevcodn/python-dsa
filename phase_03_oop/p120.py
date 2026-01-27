class Inventory:
	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)

	def remove(self, item):
		self.items.remove(item)

	def show(self):
		return self.items


inv = Inventory()
inv.add("sword")
inv.add("shield")
inv.add("potion")
print(inv.show())
inv.remove("shield")
print(inv.show())
