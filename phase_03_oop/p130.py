class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Student(Person):
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self.grade = grade

class Teacher(Person):
	def __init__(self, name, age, subject):
		super().__init__(name, age)
		self.subject = subject

student = Student("Denis", 22, "A")
teacher = Teacher("Ivan", 35, "Python")

print(student.name)
print(student.grade)
print(teacher.subject)
