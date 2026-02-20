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

    def max_depth(self, node):
        if not node:
            return 0
        left_depth = self.max_depth(node.left)
        right_depth = self.max_depth(node.right)
        return max(left_depth, right_depth) + 1
        


tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)

print(tree.max_depth(tree.root))