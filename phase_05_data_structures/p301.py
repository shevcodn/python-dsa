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
        
        current_node = self.root
        while True:
            if val < current_node.val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = TreeNode(val)
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = TreeNode(val)
                    break

    def search(self, val):
        current_node = self.root
        while current_node:
            if val == current_node.val:
                return True
            elif val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
     
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
print(tree.search(3))
print(tree.search(9))