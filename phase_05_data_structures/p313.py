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

def count_good_nodes(node, max_so_far=float('-inf')):
    if not node:
        return 0
    count = 1 if node.val >= max_so_far else 0
    new_max = max(max_so_far, node.val)
    count += count_good_nodes(node.left, new_max)
    count += count_good_nodes(node.right, new_max)
    return count
    
tree = BST()
for val in [5, 3, 7, 4, 2]:
    tree.insert(val)

print(count_good_nodes(tree.root))