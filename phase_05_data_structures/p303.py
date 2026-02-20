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

    def preorder(self, node, result):
        if node:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)


    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)
        


tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)

pre = []
tree.preorder(tree.root, pre)
print(pre)

post = []
tree.postorder(tree.root, post)
print(post)
