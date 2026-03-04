def count_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count

graph1 = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
graph2 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}

print(count_components(graph1))
print(count_components(graph2))
