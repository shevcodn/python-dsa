def topological_sort(graph):
    visited = set()
    result = []


    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        result.append(node)

    for node in graph:
        dfs(node)

    return result[::-1]

graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

print(topological_sort(graph))