def num_islands(grid):
    if not grid:
        return 0
    count = 0

    def dfs(row, col):
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '0'
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                dfs(row, col)
                count += 1

    return count


grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]

print(num_islands(grid))