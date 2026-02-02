class Animal:
	def __init__(self, name):
		self.name = name

	def meke_sound(self):
		return "Some sound"

class Dog(Animal):
	def __init__(self, name, breed):
		super().__init__(name)
		self.breed = breed

	def make_sound(self):
		return "{self.name} says Woof!"

class Cat(Animal):
	def __init__(self, name, color):
		super().__init__(name)
		self.color = color

	def make_sound(self):
		return"{self.name} says Meow!"

animals = [
	Dog("Buddy", "Golden Retriever"),
	Cat("Whiskers", "Orange"),
	Dog("Rex", "German Shepherd")
]

for animal in animals:
	print(animal.make_sound())
