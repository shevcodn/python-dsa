def max_area_islands(grid):
    if not grid:
        return 0
    max_area = 0

    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        area = 1
        area += dfs(r+1, c)
        area += dfs(r-1, c)
        area += dfs(r, c+1)
        area += dfs(r, c-1)
        return area
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    return max_area


grid = [
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,0,1,0,1],
      [0,0,0,0,1],
  ]


print(max_area_islands(grid))

grid2 = [[0,0,0], [0,0,0]]
print(max_area_islands(grid2))
    