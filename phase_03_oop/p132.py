class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		return "..."

class Dog(Animal):
	def speak(self):
		return "Woof"

class Puppy(Dog):
	def speak(self):
		return "Yip yip!"

animal = Animal("Thing")
dog = Dog("Buddy")
puppy = Puppy("Max")

print(animal.speak())
print(dog.speak())
print(puppy.speak())
print(puppy.name)
