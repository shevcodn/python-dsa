from collections import deque
import heapq

graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4), ('E', 1)],
    'C': [('D', 1)],
    'D': [],
    'E': []
}

def dfs(graph, start):
    visited = set()
    result = []

    def _dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor, _ in graph.get(node, []):
            _dfs(neighbor)

    _dfs(start)
    return result

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return distances

def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def _dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                if _dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if _dfs(node):
                return True
    return False

def topological_sort(graph):
    visited = set()
    result = []

    def _dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            _dfs(neighbor)
        result.append(node)

    for node in graph:
        _dfs(node)

    return result[::-1]

print("DFS:", dfs(graph, 'A'))
print("BFS:", bfs(graph, 'A'))
print("Dijkstra:", dijkstra(graph, 'A'))
print("Cycle:", has_cycle(graph))
print("Topo:", topological_sort(graph))

cyclic = {'A': [('B',1)], 'B': [('C',1)], 'C': [('A',1)]}
print("Cycle check:", has_cycle(cyclic))