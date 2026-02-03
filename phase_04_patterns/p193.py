import json

def read_json(filename):
	with open(filename, "r") as file:
		return json.load(file)


data = read_json("config.json")
print(data)
