import pytest
import sys

def parse_int(s):
    return int(s)

def beta_feature():
    raise NotImplementedError("Not ready")

@pytest.mark.skip(reason="not implemented yet")
def test_beta():
    assert beta_feature() == 42

@pytest.mark.skipif(sys.platform == "win32", reason="Linux  only")
def test_linux_only():
    assert True

@pytest.mark.xfail(reason="known bug")
def test_parse_bad_input():
    assert parse_int("abc") == 0

@pytest.mark.parametrize("s, expected", [
    ("42", 42),
    ("0", 0),
    ("-5", -5)
])
def test_parse_int(s, expected):
    assert parse_int(s) == expected

