def build_profile(name, **info):
	profile = {"name": name}
	profile.update(info)
	return profile

result = build_profile("Denis", age=21, city="Toronto")
print(result)
