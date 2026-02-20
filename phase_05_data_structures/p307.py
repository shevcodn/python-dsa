
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

    def is_same_tree(self, q, p):
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.is_same_tree(q.left, p.left) and self.is_same_tree(q.right, p.right)
   
    
tree1 = BST()
tree1.insert(5)
tree1.insert(3)
tree1.insert(7)

tree2 = BST()
tree2.insert(5)
tree2.insert(3)
tree2.insert(7)

tree3 = BST()
tree3.insert(5)
tree3.insert(3)
tree3.insert(9)


print(tree1.is_same_tree(tree1.root, tree2.root))
print(tree1.is_same_tree(tree1.root, tree3.root))