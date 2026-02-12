class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def draw(self, x, y):
        print(f"Drawiing {self.name} tree at ({x}, {y})")

class TreeFactory:
    def __init__(self):
        self.tree_types = {}

    def get_tree_type(self, name, color):
        key = (name, color)
        if key not in self.tree_types:
            self.tree_types[key] = TreeType(name, color)
            return self.tree_types[key]
        
    def total_types(self):
        return len(self.tree_types)

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


factory = TreeFactory()

tree1 = Tree(10, 20, factory.get_tree_type("Oak", "Green"))
tree2 = Tree(15, 25, factory.get_tree_type("Pine", "Dark Green"))
tree3 = Tree(10, 20, factory.get_tree_type("Oak", "Green"))

print(factory.total_types())