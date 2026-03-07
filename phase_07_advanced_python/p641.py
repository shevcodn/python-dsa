def calculate_total_with_tax(amount: float, tax_rate: float, quantity: int) -> float:
    subtotal = amount * quantity
    tax = subtotal * tax_rate
    return subtotal + tax


def contains_value(items: list, target) -> bool:
    for item in items:
        if item == target:
            return True
    return False


print(calculate_total_with_tax(50.0, 0.13, 3))
print(contains_value([1, 2, 3, 4], 3))
print(contains_value(["a", "b", "c"], "z"))
