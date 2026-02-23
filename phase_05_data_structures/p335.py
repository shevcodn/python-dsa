def can_finish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for a, b in prerequisites:
        graph[b].append(a)

    state = [0] * numCourses

    def dfs(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        state[node] = 2
        return False
    
    for i in range(numCourses):
        if dfs(i):
            return False
        
print(can_finish(2, [[1,0]]))
print(can_finish(2, [[1,0], [0,1]]))