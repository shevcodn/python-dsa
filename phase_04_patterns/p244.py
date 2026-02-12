class File:
    def __init__(self, name, size):
        self.size = size
        self.name = name

    def accept(self, visitor):
        return visitor.visit_file(self)

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def accept(self, visitor):
        return visitor.visit_folder(self)

class SizeCalculator:
    def visit_file(self, file):
        return file.size

    def visit_folder(self, folder):
        total = 0
        for item in folder.children:
            total += item.accept(self)
        return total

class NamePrinter:
    def visit_file(self, file):
        print(f"File: {file.name}")
    
    def visit_folder(self, folder):
        print(f"Folder: {folder.name}")

file1 = File("doc.txt", size=100)
file2 = File("pic.jpg", size=500)
folder = Folder("photos")
folder.add(file1)
folder.add(file2)

size_calc = SizeCalculator()
print(file1.accept(size_calc))
print(folder.accept(size_calc))

printer = NamePrinter()
file1.accept(printer)
folder.accept(printer)