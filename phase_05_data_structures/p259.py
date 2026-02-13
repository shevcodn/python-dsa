class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from an empty queue")
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Front from an empty queue")
    
    def is_empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.front())
print(q.dequeue())
print(q.size())