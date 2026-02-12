class File:
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print("  " * indent + f"File: {self.name}")

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def show(self, indent=0):
        print("  " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.show(indent + 1)

root = Folder("Root")
file1 = File("readme.txt")
file2 = File("config.json")

subfolder = Folder("src")
file3 = File("main.py")

subfolder.add(file3)
root.add(file1)
root.add(file2)
root.add(subfolder)

root.show()