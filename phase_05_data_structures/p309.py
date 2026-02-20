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
    
    def has_path_sum(node, target):
        if not node:
            return False
        if not node.left and not node.right:
            return node.val == target
        return (BST.has_path_sum(node.left, target - node.val) or
                BST.has_path_sum(node.right, target - node.val))
        

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)

print(BST.has_path_sum(tree.root, 8))
print(BST.has_path_sum(tree.root, 12))