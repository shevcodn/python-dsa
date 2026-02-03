def safe_get_element(lst, index):
	try:
		return lst[index]
	except IndexError:
		return "Index out of range"
	except TypeError:
		return "Not a list"

lst = [10, 20, 30]
print(safe_get_element(lst, 1))
print(safe_get_element(lst, 10))
print(safe_get_element("text", 0))
