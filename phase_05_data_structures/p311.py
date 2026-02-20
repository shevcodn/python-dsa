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

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not (min_val < node.val < max_val):
        return False
    return (is_valid_bst(node.left, min_val, node.val) and
            is_valid_bst(node.right, node.val, max_val))

tree = BST()
for val in [5, 3, 7, 1, 4]:
    tree.insert(val)

print(is_valid_bst(tree.root))

tree.root.right.left = TreeNode(2)
print(is_valid_bst(tree.root))

