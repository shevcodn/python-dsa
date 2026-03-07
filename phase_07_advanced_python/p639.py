def calculate_total(amounts: list) -> float:
    return sum(amounts)


def apply_discount(prices: list, discount: float) -> list:
    return [p * (1 - discount) for p in prices]


def get_tax(amount: float, rate: float) -> float:
    return amount * rate


print(calculate_total([100, 200, 300]))
print(apply_discount([100, 200, 300], 0.1))
print(get_tax(1000.0, 0.13))
