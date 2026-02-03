def merge_dicts(dict1, dict2):
	result = dict1.copy()
	result.update(dict2)
	return result

d1 = {"name": "Denis", "age": 21}
d2 = {"age": 22, "city": "Toronto"}

result = merge_dicts(d1, d2)
print(result)


