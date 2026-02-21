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

def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return height(root) != -1

tree = BST()
for val in [5, 3, 7, 1, 4]:
    tree.insert(val)

print(is_balanced(tree.root)) 

tree2 = BST()
for val in [5, 3, 7]:
    tree2.insert(val)
tree2.root.right.right = TreeNode(9)
tree2.root.right.right.right = TreeNode(11)

print(is_balanced(tree2.root))

