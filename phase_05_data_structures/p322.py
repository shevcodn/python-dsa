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

def range_sum_bst(node, low, high):
    if not node:
        return 0
    total = 0
    if low <= node.val <= high:
        total += node.val
    if node.val > low:
        total += range_sum_bst(node.left, low, high)
    if node.val < high:
        total += range_sum_bst(node.right, low, high)
    return total

tree = BST()
for val in [5, 3, 7, 1, 4, 8]:
    tree.insert(val)

print(range_sum_bst(tree.root, 3, 7))
print(range_sum_bst(tree.root, 1, 4))