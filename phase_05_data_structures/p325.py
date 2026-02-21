class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class AdvancedBST:
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

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node
    
    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def search(self, val):
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False
    
    def delete(self, val):
        self.root = self._delete_recursively(self.root, val)

    def _delete_recursively(self, node, val):
        if not node:
            return node
        if val < node.val:
            node.left = self._delete_recursively(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursively(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_recursively(node.right, temp.val)
        return node
        
    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
    
    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def is_balanced(self, node):
        if not node:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.is_balanced(node.left) and self.is_balanced(node.right)
    
    def kth_smallest(self, node, k):
        if not node:
            return None
        left_count = self.count_nodes(node.left)
        if k <= left_count:
            return self.kth_smallest(node.left, k)
        elif k == left_count + 1:
            return node.val
        else:
            return self.kth_smallest(node.right, k - left_count - 1)
        
    def range_sum(self, node, low, high):
        if not node:
            return 0
        if node.val < low:
            return self.range_sum(node.right, low, high)
        elif node.val > high:
            return self.range_sum(node.left, low, high)
        else:
            return node.val + self.range_sum(node.left, low, high) + self.range_sum(node.right, low, high)
        
bst = AdvancedBST()
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)


print(bst.inorder(bst.root))
print(bst.height(bst.root))
print(bst.is_balanced(bst.root))
print(bst.kth_smallest(bst.root, 3))
print(bst.range_sum(bst.root, 3, 7))
print(bst.search(6))
bst.delete(5)
print(bst.inorder(bst.root))