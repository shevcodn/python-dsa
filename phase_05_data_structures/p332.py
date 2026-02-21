def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return False
            if not dfs(neighbor, node):
                return False
        return True
    
    return dfs(0, -1) and len(visited) == n

print(valid_tree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(valid_tree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))