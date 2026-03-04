from collections import deque

def count_and_max(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    max_size = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if grid[r][c] == 0 or (r, c) in visited:
            return 0
        visited.add((r, c))
        return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                size = dfs(r, c)
                count += 1
                max_size = max(max_size, size)

    return count, max_size


def has_path(graph, src, dst):
    visited = set()
    queue = deque([src])
    while queue:
        node = queue.popleft()
        if node == dst:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False


def shortest_path(graph, src, dst):
    visited = set()
    queue = deque([(src, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == dst:
            return dist
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
    return -1



grid = [[1,1,0,0],[1,0,0,1],[0,0,1,1],[0,1,1,0]]
print(count_and_max(grid))

graph = {0:[1,2], 1:[3], 2:[3], 3:[4], 4:[]}
print(has_path(graph, 0, 4))
print(has_path(graph, 2, 1))

graph2 = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2,4], 4:[3]}
print(shortest_path(graph2, 0, 4))
