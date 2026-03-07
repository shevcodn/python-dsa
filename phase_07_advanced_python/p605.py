import json

def greet(name):
    print(f"Hello, {name}!")

def save_data(path, data):
    with open(path / "data.json", "w") as f:
        json.dump(data, f)

def load_data(path):
    with open(path / "data.json") as f:
        return json.load(f)
    
def test_greet(capsys):
    greet("Denis")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Denis!\n"

def test_save_load(tmp_path):
    data = {"name": "Denis", "score": 100}
    save_data(tmp_path, data)
    result = load_data(tmp_path)
    assert result == data

