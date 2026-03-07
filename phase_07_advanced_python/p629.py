from typing import Callable, Any

def apply(value: float, func: Callable[[float], float]) -> float:
    return func(value)

def run_twice(x: float, func: Callable[[int], int]) -> None:
    func(x)
    func(x)

def log_anything(value: Any) -> None:
    print(f"LOG: {value}")

print(apply(10.0, lambda x: x * 2))
run_twice(5, lambda x: print(f"Value: {x}"))
log_anything({"key": "value", "number": 42})
