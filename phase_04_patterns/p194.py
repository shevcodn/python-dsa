import json

def write_json(filename, data):
	with open(filename, "w") as file:
		json.dump(data, file, indent=2)


data = {"name": "Denis", "tasks": 193}
write_json("progress.json", data)
