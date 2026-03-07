import pytest

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        if b == 0:
            raise ValueError("Cannot multiply by zero")
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)