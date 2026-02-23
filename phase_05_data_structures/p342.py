class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = []

def clone_graph(node):
    if not node:
        return None
    mapping = {}
    def dfs(n):
        if n in mapping:
            return mapping[n]
        copy = Node(n.val)
        mapping[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node)
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n3, n1]

copy = clone_graph(n1)
print(copy.val)
print([n.val for n in copy.neighbors])