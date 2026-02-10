class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Bird:
    def speak(self):
        print("Tweet!")

def create_animal(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    elif animal_type == "bird":
        return Bird()
    else:
        raise ValueError("Unknown animal type")

dog = create_animal("dog")
cat = create_animal("cat")
bird = create_animal("bird")

dog.speak()
cat.speak()
bird.speak()