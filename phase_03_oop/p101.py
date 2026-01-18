class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def introduce(self):
		return f"Hi, I'm {self.name} and I'm {self.age} years old"

p = Person("Denis", 22)
print(p.name)
print(p.age)
print(p.introduce())
