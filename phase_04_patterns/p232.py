class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def save(self):
        return self.text
    
    def restore(self, memento):
        self.text = memento

editor = TextEditor()

editor.write("Hello")
print(editor.text)

saved = editor.save()

editor.write(" World")
print(editor.text)

editor.restore(saved)
print(editor.text)