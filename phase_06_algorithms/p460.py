def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for a, b in prerequisites:
        graph[b].append(a)

    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in visited:
            return True
        if node in rec_stack:
            return False
        rec_stack.add(node)
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        rec_stack.remove(node)
        visited.add(node)
        return True
    
    for i in range(num_courses):
        if i not in visited:
            if not dfs(i):
                return False
    
    return True

print(can_finish(2, [[1, 0]]))
print(can_finish(2, [[1, 0], [0, 1]]))
print(can_finish(3, [[1, 0], [2, 1]]))

