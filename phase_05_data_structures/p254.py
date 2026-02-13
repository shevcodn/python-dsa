class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]
    
    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)
    
q = Queue()
q.enqueue("Вася")
q.enqueue("Петя")
q.enqueue("Коля")
print(q.front())
print(q.dequeue())
print(q.size())
print(q.is_empty())
