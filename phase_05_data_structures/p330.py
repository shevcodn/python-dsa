class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def clone_graph(node, visited=None):
    if not node:
        return None
    if visited is None:
        visited = {}
    if node in visited:
        return visited[node]
    
    clone = Node(node.val)
    visited[node] = clone

    for neighbor in node.neighbors:
        clone.neighbors.append(clone_graph(neighbor, visited))

    return clone

n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

copy = clone_graph(n1)
print(copy.val)
print([n.val for n in copy.neighbors])
print(copy is n1)
