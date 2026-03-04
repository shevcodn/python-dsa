def pacific_atlantic(heights):
    if not heights:
        return []
    
    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def bfs(starts, visited):
        queue = list(starts)
        visited.update(starts)
        while queue:
            r, c = queue.pop(0)
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    pac_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atl_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]


    bfs(pac_starts, pacific)
    bfs(atl_starts, atlantic)

    return [[r, c] for r, c in pacific if (r, c) in atlantic]

print(pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))