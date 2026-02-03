class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		if age < 0:
			raise ValueError("Age cannot be negative")

class Student(Person):
	def __init__(self, name, age, student_id):
		super().__init__(name, age)
		self.student_id = student_id
		self.courses = []

	def add_course(self, course_name):
		self.courses.append(course_name)

	def get_courses(self):
		return self.courses

class Course:
	def __init__(self, name, credits):
		self.name = name
		self.credits = credits

	def __str__(self):
		return f"{self.name} ({self.credits} credits)"

student = Student("Denis", 21, "S12345")
student.add_course("Python Programming")
student.add_course("Data Structures")
print(student.name)
print(student.age)
print(student.get_courses())
