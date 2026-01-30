class Dog:
	def speak(self):
		return "Woof"

class Cat:
	def speak(self):
		return "Meow"


def create_animal(animal_type):
	if animal_type == "dog":
		return Dog()
	elif animal_type == "cat":
		return Cat()
	else:
		return None

dog = create_animal("dog")
cat = create_animal("cat")

print(dog.speak())
print(cat.speak())
