class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        current = self.root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break

def floor_ceiling(root, target):
    floor = None
    ceiling = None
    
    while root:
        if root.val == target:
            return root.val, root.val
        elif root.val < target:
            floor = root.val
            root = root.right
        else:
            ceiling = root.val
            root = root.left

    return floor, ceiling



tree = BST()
for val in [5, 3, 7, 1, 4]:
    tree.insert(val)

print(floor_ceiling(tree.root, 6))
print(floor_ceiling(tree.root, 3))
print(floor_ceiling(tree.root, 0))