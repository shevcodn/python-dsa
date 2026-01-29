class Animal:
	def __init__(self, name):
		self.name = name

	def make_sound(self):
		return "Some sound"

class Dog(Animal):
	def make_sound(self):
		parent_sound = super().make_sound()
		return parent_sound + " Woof!"

dog = Dog("Buddy")
print(dog.make_sound())
