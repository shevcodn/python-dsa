from typing import TypeVar, List

T = TypeVar('T')

def first_item(items: List[T]) -> T:
    if not items:
        raise ValueError("List is empty")
    return items[0]

def last_item(items: List[T]) -> T:
    if not items:
        raise ValueError("List is empty")
    return items[-1]

def repeat(value: T, times: int) -> List[T]:
    return [value] * times

print(first_item([1, 2, 3]))
print(last_item(["a", "b", "c"]))
print(repeat(5, 3))