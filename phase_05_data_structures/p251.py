class DynamicArray:
    def __init__(self):
        self.data = []
        self.size = 0

    def append(self, item):
        self.data.append(item)
        self.size += 1

    def get(self, index):
        self.index = index
        return self.data[index]
    
    def remove(self, index):
        self.index = index
        del self.data[index]

    def length(self):
        return self.size

    def __str__(self):
        return str(self.data)
    
arr = DynamicArray()
arr.append(10)
arr.append(20)
arr.append(30)
print(arr.length())
print(arr.get(1))
arr.remove(0)
print(arr)

