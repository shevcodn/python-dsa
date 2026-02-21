def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return True
    if start in visited:
        return False
    visited.add(start)
    for neighbor in graph[start]:
        if has_path(graph, neighbor, end, visited):
            return True
    return False
    
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

print(has_path(graph, 'A', 'D'))
print(has_path(graph, 'D', 'E'))
print(has_path(graph, 'D', 'C'))
