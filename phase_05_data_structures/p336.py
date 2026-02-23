from collections import defaultdict

def count_components(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count

print(count_components(5, [[0,1], [1,2], [3,4]]))
print(count_components(5, [[0,1], [1,2], [2,3], [3,4]]))
print(count_components(4, []))
