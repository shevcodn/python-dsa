class Number:
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()
    
class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()
    
expr = Add(Number(5), Number(3))
print(expr.interpret())

expr2 = Add(Subtract(Number(10), Number(2)), Number(5))
print(expr2.interpret())
