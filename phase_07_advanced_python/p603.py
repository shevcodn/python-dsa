import pytest

def is_even(n):
    return n % 2 == 0

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-5, False)
])
def test_is_even(n, expected):
    assert is_even(n) == expected

@pytest.mark.parametrize("value, min_val, max_val, expected", [
    (5, 0, 10, 5),
    (15, 0, 10, 10),
    (-5, 0, 10, 0)
])
def test_clamp(value, min_val, max_val, expected):
    assert clamp(value, min_val, max_val) == expected