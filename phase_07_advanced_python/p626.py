def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_adult(age: int) -> bool:
    return age >= 18

def log_message(message: str) -> None:
    print(f"LOG: {message}")

def get_balance(account_id: str, amount: float) -> float:
    return round(amount * 1.05, 2)

print(greet("Denis"))
print(add(5, 7))
print(is_adult(20))
log_message("This is test log")
print(get_balance("acc123", 1000.0))


