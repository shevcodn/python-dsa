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

def serialize(root):
    if not root:
        return None
    return [root.val, serialize(root.left), serialize(root.right)]

def deserialize(data):
    if data is None:
        return None
    node = TreeNode(data[0])
    node.left = deserialize(data[1])
    node.right = deserialize(data[2])
    return node

tree = BST()
for val in [5, 3, 7, 1, 4]:
    tree.insert(val)

data = serialize(tree.root)
print(data)

root2 = deserialize(data)
print(inorder(root2))
