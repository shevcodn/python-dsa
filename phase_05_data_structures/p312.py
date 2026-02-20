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

def right_side_view(node):
    if not node:
        return []
    result = []
    queue = [node]
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current = queue.pop(0)
            if i == level_size - 1:
                result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return result

tree = BST()
for val in [5, 3, 7, 1, 4]:
    tree.insert(val)

print(right_side_view(tree.root))
