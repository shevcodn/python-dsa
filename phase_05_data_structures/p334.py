from collections import deque

def oranges_rotting(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1
    if fresh_count == 0:
        return 0
    
    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))

    return -1 if fresh_count > 0 else minutes -1 
    


grid1 = [[2,1,1],[1,1,0],[0,1,1]]
print(oranges_rotting(grid1))

grid2 = [[2,1,1],[0,1,1],[1,0,1]]
print(oranges_rotting(grid2))

grid3 = [[0,2]]
print(oranges_rotting(grid3))