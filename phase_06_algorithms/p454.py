def has_path(graph, src, dst, visited=None):
    if visited is None:
        visited = set()

    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)

    for neighbor in graph.get(src, []):
        if has_path(graph, neighbor, dst, visited):
            return True
    
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(has_path(graph, 'A', 'F'))
print(has_path(graph, 'D', 'F'))
print(has_path(graph, 'A', 'A'))