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
    
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def invert_tree(node):
    if node:
        node.left, node.right = invert_tree(node.right), invert_tree(node.left)
    return node

tree1 = BST()
tree1.insert(5)
tree1.insert(3)
tree1.insert(7)

print(inorder(tree1.root))
invert_tree(tree1.root)
print(inorder(tree1.root))