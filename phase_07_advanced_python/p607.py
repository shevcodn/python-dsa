from unittest.mock import patch
import datetime
from unittest.mock import mock_open

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    return "Good evening!"

def read_config(path):
    with open(path) as f:
        return f.read().strip()
    
def test_greeting_morning():
    with patch('datetime.datetime') as mock_dt:
        mock_dt.now.return_value.hour = 9
        assert get_greeting() == "Good morning!"

def test_greeting_afternoon():
    with patch('datetime.datetime') as mock_dt:
        mock_dt.now.return_value.hour = 15
        assert get_greeting() == "Good afternoon!"

def test_read_config():
    with patch("builtins.open", mock_open(read_data="production")):
        result = read_config("config.txt")
        assert result == "production"

       