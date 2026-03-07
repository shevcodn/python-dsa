from hypothesis import given
from hypothesis import strategies as st

def sort_list(lst):
    return sorted(lst)

def reverse_string(s):
    return s[::-1]

@given(st.lists(st.integers()))
def test_sort_list(lst):
    result = sort_list(lst)
    assert len(result) == len(lst)

@given(st.lists(st.integers(), min_size=1))
def test_sort_ordered(lst):
    result = sort_list(lst)
    assert result[0] <= result[-1]

@given(st.text())
def test_reverse_twice(s):
    assert reverse_string(reverse_string(s)) == s