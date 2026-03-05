class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return validate(node.left, min_val, node.val) and \
                validate(node.right, node.val, max_val)

    return validate(root, float('-inf'), float('inf'))

root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(4)

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(7)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(6)

print(is_valid_bst(root1))
print(is_valid_bst(root2))
print(is_valid_bst(None))