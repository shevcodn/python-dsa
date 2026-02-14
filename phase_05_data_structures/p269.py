def word_count(text):
    words = text.split()
    return len(words)

result = word_count("Hello world hello python world hello")
print(result)