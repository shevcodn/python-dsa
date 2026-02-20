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


def lca(node, p, q):
    if not node:
        return None
    if node.val > p and node.val > q:
        return lca(node.left, p, q)
    if node.val < p and node.val < q:
        return lca(node.right, p, q)
    return node.val

tree = BST()
for val in [5, 3, 7, 1, 4]:
    tree.insert(val)

print(lca(tree.root, 1, 4))  # 3
print(lca(tree.root, 1, 7))  # 5
print(lca(tree.root, 3, 4))  # 3