def validate_age(age):
	if age < 0:
		raise ValueError("Age cannot be negative")
	if age > 120:
		raise ValueError("Age too high")
	return True

print(validate_age(25))
print(validate_age(-5))
print(validate_age(150))
