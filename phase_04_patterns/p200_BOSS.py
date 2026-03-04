import csv
import json


def calculate_average(scores):
	return sum(scores) / len(scores)

def get_status(average):
	if average >= 75:
		return "Pass"
	else:
		return "Fail"

def process_students(filename):
	results = []

	with open(filename, "r") as file:
		reader = csv.DictReader(file)

		for row in reader:

			name = row["name"]

			scores = [
				int(row["math"]),
				int(row["english"]),
				int(row["science"])
			]


			average = calculate_average(scores)
			status = get_status(average)

			results.append({
				"name": name,
				"average": average,
				"status": status
			})
	return results

def save_results(results, json_filename, txt_filename):
	with open(json_filename, "w") as file:
		json.dump(results, file, indent=2)

	with open(txt_filename, "w") as file:
		file.write("=== STUDENT GRADE REPORT ===\n")
		for student in results:
			name = student["name"]
			avg = student["average"]
			status = student["status"]
			file.write(f"{name}: {avg:.2f} - {status}\n")


def main():
	try:
		results = process_students("students.csv")
		save_results(results, "results.json", "report.txt")
		print("Processing complete!")
	except FileNotFoundError:
		print("Error: students.csv not found")
	except Exception as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()
