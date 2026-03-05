class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root):
    def dfs(node, max_so_far):
        if not node:
            return 0
        
        count = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)

        count += dfs(node.left, new_max)
        count += dfs(node.right, new_max)

        return count
    
    return dfs(root, float('-inf'))

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print(good_nodes(root))
print(good_nodes(TreeNode(1)))