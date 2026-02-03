class Person:
	def __init__(self, name, age):
		if age < 0:
			raise ValueErorr("Age cannot be negative")
		self.name = name
		self.age = age

	def __str__(self):
		return f"Person: {self.name}, Age: {self.age}"


class Teacher(Person):
	def __init__(self, name, age, subject):
		super().__init__(name, age)
		self.subject = subject

	def __str__(self):
		return f"Teacher {self.name} teaches {self.subject}"

class Student(Person):
	def __init__(self, name, age, student_id):
		super().__init__(name, age)
		self.student_id = student_id
		self.grades = {}

	def add_grade(self, subject, grade):
		self.grades[subject] = grade

	def get_average(self):
		total = sum(self.grades.values())
		count = len(self.grades)
		return total / count


	def __str__(self):
		return f"Student {self.name} (ID: {self.student_id})"

class School:
	def __init__(self, name):
		self.name = name
		self.teachers = []
		self.students = []

	def add_teacher(self, teacher):
		self.teachers.append(teacher)

	def add_student(self, student):
		self.students.append(student)

	def get_total_people(self):
		return len(self.students + self.teachers)

school = School("Toronto Hight School")

teacher = Teacher("Mr.Smith", 45, "Math")
student = Student("Denis", 21, "S001")

school.add_teacher(teacher)
school.add_student(student)

student.add_grade("Math", 95)
student.add_grade("Python", 100)

print(school.get_total_people())
print(student.get_average())
print(teacher)
print(student)
