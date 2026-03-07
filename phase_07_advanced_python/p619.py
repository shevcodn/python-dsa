import pytest
from unittest.mock import Mock

class User:
    def __init__(self, name, email, role="user", balance=0):
        self.name = name
        self.email = email
        self.role = role
        self.balance = balance



def make_user(**kwargs):
    defaults = {"name": "Denis", "email": "denis@test.com", "role": "user", "balance": 100}
    defaults.update(kwargs)
    return User(**defaults)

def test_default_user():
    user = make_user()
    assert user.name == "Denis"
    assert user.balance == 100

def test_admin_user():
    user = make_user(role="admin", balance=1000)
    assert user.role == "admin"

def test_custom_user():
    user = make_user(name="Pavel", email="pavel@test.com")
    assert user.name == "Pavel"
    assert user.email == "pavel@test.com"

def test_multiple_users():
    users = [make_user(name=f"User{i}") for i in range(3)]
    assert len(users) == 3
    assert users[0].name == "User0"
    assert users[1].name == "User1"
    assert users[2].name == "User2"



