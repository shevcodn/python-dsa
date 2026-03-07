def calculate_subtotal(items: list) -> float:
    return sum(i["price"] for i in items)


def apply_premium_discount(subtotal: float, is_premium: bool) -> float:
    if is_premium:
        return subtotal * 0.9
    return subtotal


def add_tax(amount: float) -> float:
    return amount * 1.13


def print_order_summary(name: str, total: float) -> None:
    print(f"Order for {name}: ${total:.2f}")


def process_order(order: dict) -> float:
    subtotal = calculate_subtotal(order["items"])
    discounted = apply_premium_discount(subtotal, order["user"]["is_premium"])
    total = add_tax(discounted)
    print_order_summary(order["user"]["name"], total)
    order["status"] = "processed"
    return order


order = {
    "items": [{"price": 100}, {"price": 200}, {"price": 50}],
    "user": {"name": "Denis", "is_premium": True}
}
process_order(order)

