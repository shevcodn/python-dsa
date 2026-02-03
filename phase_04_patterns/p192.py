import csv

def write_csv(filename, data):
	with open(filename, "w", newline='') as file:
		fieldnames = data[0].keys()
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(data)

data = [
	{"name": "Denis", "age": "21", "city": "Toronto"},
	{"name": "Bob", "age": "30", "city": "London"}
]


write_csv("output.csv", data)
