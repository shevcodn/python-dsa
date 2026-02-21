
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result += dfs(graph, neighbor, visited)

    return result 


graph = {                                   
    'A': ['B', 'C'],                    
    'B': ['A', 'D', 'E'],
    'C': ['A'],                                                                                                                       
    'D': ['B'],
    'E': ['B']                                                                                                                        
}
 
print(dfs(graph, 'A'))