class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __str__(self):
		return f"{self.title} by {self.author}"

class Library:
	def __init__(self, name):
		self.name = name
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def show_books(self):
		for book in self.books:
			print(book)


lib = Library("City Library")

lib.add_book(Book("1984", "Orwell"))
lib.add_book(Book("Dune", "Herbert"))
lib.add_book(Book("Foundation", "Asimov"))

lib.show_books()
