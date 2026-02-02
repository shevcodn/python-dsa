class Person:
	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value < 0 or value > 150:
			raise ValueError("Invalid Age")
		self._age = value


	@property
	def birth_year(self):
		return 2026 - self._age

p = Person("Denis", 21)
print(p.age)
print(p.birth_year)

p.age = 25
print(p.birth_year)
