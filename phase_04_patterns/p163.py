class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __lt__(self, other):
		return self.age < other.age

p1 = Person("Denis", 21)
p2 = Person("Alex", 25)

print(p1 < p2)
print(p2 < p1)
