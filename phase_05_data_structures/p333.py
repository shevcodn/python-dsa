def num_islands(grid):
    if not grid:
        return 0
    count = 0

    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
        
grid = [["1","1","0"],["0","1","0"],["0","0","1"]]
print(num_islands(grid))