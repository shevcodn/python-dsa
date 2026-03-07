from unittest.mock import Mock, patch

def fetch_rate(currency):
    raise ConnectionError("No internet")

def get_exchange(amount, currency):
    rate = fetch_rate(currency)
    return round(amount * rate, 2)

def test_fetch_fails():
    with patch("p608.fetch_rate") as mock_fetch:
        mock_fetch.side_effect = ConnectionError("No Internet")
        try:
            get_exchange(100, "USD")
            assert False
        except ConnectionError as e:
            assert str(e) == "No Internet"
            pass

def test_multiple_calls():
    mock = Mock()
    mock.side_effect = [10.5, 11.0, 9.8]
    assert mock() == 10.5
    assert mock() == 11.0
    assert mock() == 9.8

    