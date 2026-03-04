class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


class DataProcessor:
    def __init__(self):
        self.data = []
        self.stack = Stack()

    def add(self, item):
        self.data.append(item)
        self.stack.push(item)

    def process(self):
        return self.stack.pop()

    def search(self, target):
        return True if target in self.data else False

    def size(self):
        return self.stack.size()


dp = DataProcessor()
dp.add(5)
dp.add(3)
dp.add(8)
dp.add(1)

print(dp.search(3))
print(dp.search(9))
print(dp.size())
print(dp.process())
print(dp.size())                                                                                                                         
