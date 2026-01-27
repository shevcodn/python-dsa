class Dog:
	def __init__(self, name, age):
		self.name = "buddy"
		self.age = 3

	def bark(self):
		return "Woof!"

	def get_info(self):
		return f"{self.name} is {self.age} years old"

	def have_birthday(self):
		self.age = self.age + 1
		return self.age

buddy = Dog("Buddy", 3)
print(buddy.bark())
print(buddy.get_info())
buddy.have_birthday()
print(buddy.get_info())
