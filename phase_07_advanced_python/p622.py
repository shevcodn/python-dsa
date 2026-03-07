import pytest
from unittest.mock import Mock, MagicMock

class UserRepository:
    def __init__(self, db):
        self.db = db

    def find_by_id(self, user_id):
        row = self.db.execute("SELECT * FROM users WHERE id = ?", (user_id, ))
        return row.fetchone()
    
    def create(self, name, email):
        self.db.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        return self.db.lastrowid
    
    def delete(self, user_id):
        rows = self.db.execute("DELETE FROM users WHERE id = ?", (user_id,))
        return rows.rowcount
    
@pytest.fixture
def db():
    return MagicMock()

@pytest.fixture
def repo(db):
    return UserRepository(db)

def test_find_user(repo, db):
    db.execute.return_value.fetchone.return_value = {"id": 1, "name": "Denis"}
    result = repo.find_by_id(1)
    assert result ["name"] == "Denis"
    db.execute.assert_called_once_with("SELECT * FROM users WHERE id = ?", (1, ))

def test_create_user(repo, db):
    db.lastrowid = 1
    result = repo.create("Denis", "denis@test.com")
    assert result == 1

def test_delete_user(repo, db):
    db.execute.return_value.rowcount = 1
    result = repo.delete(1)
    assert result == 1
    db.execute.assert_called_once_with("DELETE FROM users WHERE id = ?", (1,))