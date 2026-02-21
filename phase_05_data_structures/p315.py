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
    
def max_path_sum(root):
    max_sum = float('-inf')

    def non_local(node):
        nonlocal max_sum
        if not node:
            return 0
        left_sum = max(0, non_local(node.left))
        right_sum = max(0, non_local(node.right))
        max_sum = max(max_sum, node.val + left_sum + right_sum)
        return node.val + max(left_sum, right_sum)
    non_local(root)
    return max_sum

tree = BST()
for val in [5, 3, 7, 1, 4]:
    tree.insert(val)
tree.root.left.left = TreeNode(-1)

print(max_path_sum(tree.root))