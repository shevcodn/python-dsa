class Person:
	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def age(self):
		return self._age

	@staticmethod
	def is_adult(age):
		if age >= 18:
			return True
		else:
			return False

p = Person("Denis", 21)

print(Person.is_adult(21))
print(Person.is_adult(15))
print(p.is_adult(21))


