from typing import Optional, Union

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Denis"
    return None

def parse_amount(value: Union[str, float]) -> Optional[float]:
    try:
        return float(value)
    except ValueError:
        return None
    
def get_fee(amount: float, discount: Optional[float] = None) -> float:
    if discount is None:
        return amount * 0.02
    return amount * 0.02 * (1 - discount)

print(find_user(1))
print(find_user(2))
print(parse_amount("100.5"))
print(parse_amount("abc"))
print(get_fee(1000.0))
print(get_fee(1000.0, discount=0.1))
