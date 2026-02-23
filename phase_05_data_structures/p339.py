def pacific_atlantic(heights):
    if not heights:
        return []
    
    rows, cols = len(heights), len(heights[0])

    def dfs(r, c, visited):
        visited.add((r, c))
        for dr, dc in [(1,0), (-1,0), (0,1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and
                heights[nr][nc] >= heights[r][c]
            ):
                dfs(nr, nc, visited)

    pacific_atlantic_cells = set()
    pacific_atlantic_cellc = set()
    for i in range(rows):
        dfs(i, 0, pacific_atlantic_cells)
        dfs(i, cols - 1, pacific_atlantic_cellc)
    for j in range(cols):
        dfs(0, j, pacific_atlantic_cells)
        dfs(rows - 1, j, pacific_atlantic_cellc)

    return sorted(pacific_atlantic_cells & pacific_atlantic_cellc)

heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
  ]

print(pacific_atlantic(heights))