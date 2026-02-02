class Person:
	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def age(self):
		return self._age

	@classmethod
	def from_birth_year(cls, name, birth_year):
		age = 2026 - birth_year
		return cls(name, age)

p1 = Person("Denis", 21)
print(p1.age)

p2 = Person.from_birth_year("Alex", 2000)
print(p2.age)
