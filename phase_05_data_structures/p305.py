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

    def count_nodes(self, node):
        if not node:
            return 0
        left_count = self.count_nodes(node.left)
        right_count = self.count_nodes(node.right)
        return left_count + right_count + 1        


tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)

print(tree.count_nodes(tree.root))