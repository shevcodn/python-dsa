def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for a, b in prerequisites:
        graph[b].append(a)

    state = [0] * num_courses

    def has_cycle(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = 2
        return False
    
    for i in range(num_courses):
        if has_cycle(i):
            return False
        return True
    
print(can_finish(2, [[1,0]]))
print(can_finish(2, [[1,0], [0, 1]]))
print(can_finish(3, [[1, 0], [2, 1]]))

