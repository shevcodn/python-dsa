class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def clone(self):
        return Document(self.title, self.content)

original = Document("Report", "Sales data for Q1")
print(f"Original: {original.title} - {original.content})")

copy = original.clone()
print(f"Copy: {copy.title} - {copy.content}")

copy.title = "Report Copy"
copy.content = "Modified Data"

print(f"Original after: {original.title} - {original.content}")
print(f"Copy after: {copy.title} - {copy.content}")

print(original is copy)