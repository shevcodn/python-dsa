class Book:
	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year

	def __str__(self):
		return f"{self.title} by {self.author}"

	def __repr__(self):
		return f"Book('{self.title}', '{self.author}', {self.year})"


b = Book("1984", "Orwell", 1949)
print(b)
print(repr(b))
