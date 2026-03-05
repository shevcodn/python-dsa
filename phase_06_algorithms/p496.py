class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(lowest_common_ancestor(root, TreeNode(5), TreeNode(1)).val)
print(lowest_common_ancestor(root, TreeNode(5), TreeNode(4)).val)
print(lowest_common_ancestor(root, TreeNode(6), TreeNode(4)).val)