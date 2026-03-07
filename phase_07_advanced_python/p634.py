from typing import Literal, overload

Direction = Literal["buy", "sell", "hold"]

def execute_order(direction: Direction, amount: float) -> str:
    if direction == "buy":
        return f"Order: {direction} {amount} units"
    elif direction == "sell":
        return f"Order: {direction} {amount} units"
    elif direction == "hold":
        return "Order: hold"
    else:
        raise ValueError("Invalid direction")
    
@overload
def parse(value: str) -> str: ...
@overload
def parse(value: int) -> int: ...

def parse(value):
    if isinstance(value, str):
        return f"Parsed string: {value}"
    elif isinstance(value, int):
        return value * 2
    else:
        raise ValueError("Unsupported type")
    
print(execute_order("buy", 100.0))
print(execute_order("sell", 50.0))
print(execute_order("hold", 0.0))
print(parse("Hello"))
print(parse(10))
