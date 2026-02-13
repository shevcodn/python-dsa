class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.size())
print(s.is_empty())