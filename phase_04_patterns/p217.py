class Calculator:
    def __init__(self):
        self.result = 0
        self.history = []

    def execute_command(self, command):
        command.execute(self)
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo(self)
        else:
            print("No commands to undo")
            
class AddCommand:
    def __init__(self, value):
        self.value = value

    def execute(self, calculator):
        calculator.result += self.value

    def undo(self, calculator):
        calculator.result -= self.value

class SubtractCommand:
    def __init__(self, value):
        self.value = value

    def execute(self, calculator):
        calculator.result -= self.value

    def undo(self, calculator):
        calculator.result += self.value

class MultiplyCommand:
    def __init__(self, value):
        self.value = value

    def execute(self, calculator):
        calculator.result *= self.value

    def undo(self, calculator):
        if self.value != 0:
            calculator.result /= self.value
        else:
            print("Cannot undo multiplication by zero")

class DivideCommand:
    def __init__(self, value):
        self.value = value

    def execute(self, calculator):
        if self.value != 0:
            calculator.result /= self.value
        else:
            print("Cannot divide by zero")

    def undo(self, calculator):
        calculator.result *= self.value

calc = Calculator()

calc.execute_command(AddCommand(10))
print(calc.result)

calc.execute_command(SubtractCommand(5))
print(calc.result)

calc.execute_command(MultiplyCommand(2))
print(calc.result)

calc.execute_command(DivideCommand(3))
print(calc.result)