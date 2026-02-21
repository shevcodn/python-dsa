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

def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def merge_trees(root1, root2):
    list1 = inorder(root1)
    list2 = inorder(root2)
    return sorted(list1 + list2)

tree = BST()
for val in [5, 3, 7]:
    tree.insert(val)

tree2 = BST()
for val in [4, 2, 6]:
    tree2.insert(val)

print(merge_trees(tree.root, tree2.root))
