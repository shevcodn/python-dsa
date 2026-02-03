import os

def file_exists(filename):
	if os.path.exists(filename):
		return True
	else:
		return False

print(file_exists("test.txt"))
print(file_exists("missing.txt"))
