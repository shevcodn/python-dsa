def analyze_scores(scores):
	total = 0
	count = len(scores)
	highest = scores[0]
	lowest = scores[0]
	passing = 0
	for grade in scores:
		total = total + grade
		if grade > highest:
			highest = grade
		if grade < lowest:
			lowest = grade
		if grade >= 80:
			passing = passing + 1

	return {
		"count": count,
		"sum": total,
		"average": total / count,
		"highest": highest,
		"lowest": lowest,
		"passing": passing
	}

print(analyze_scores([85, 90, 78, 92, 88, 76, 95, 89]))
print(analyze_scores([100, 50, 75]))
