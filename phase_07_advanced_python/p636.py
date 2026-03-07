

FEE_RATE = 0.023
DISCOUNT_RATE = 0.05


def add_values(first, second):
    return first + second if first is not None and second is not None else 0


def calculate_fee(price, quantity, cost):
    return price * quantity * FEE_RATE - cost * DISCOUNT_RATE


def is_user_valid(user):
    return user.get("a") and user.get("b") is not None and user.get("c", 0) > 0

   

print(add_values(5, 3))
print(calculate_fee(1000, 2, 500))
print(is_user_valid({"a": True, "b": "ok", "c": 1}))
