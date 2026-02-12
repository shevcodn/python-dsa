class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.books):
            raise StopIteration
        else:
            book = self.books[self.index]
            self.index += 1
        return book
    
library = Library()
library.add_book(Book("1984"))
library.add_book(Book("Brave New World"))
library.add_book(Book("Fahrenheit 451"))

for book in library:
    print(book.title)