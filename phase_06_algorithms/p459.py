class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):
    if not node:
        return None
    
    clones = {}

    def dfs(n):
        if n in clones:
            return clones[n]

        clone = Node(n.val)
        clones[n] = clone

        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.neighbors = [n2, n3]
n2.neighbors = [n1]
n3.neighbors = [n1]

copy = clone_graph(n1)
print(copy.val)
print([n.val for n in copy.neighbors])
print(copy is n1)    