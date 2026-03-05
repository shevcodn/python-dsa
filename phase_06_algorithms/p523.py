def longest_increasing_path(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    memo = {}

    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        
        best = 1
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))

        memo[(r, c)] = best
        return best
    
    return max(dfs(r, c) for r in range(rows) for c in range(cols))

matrix1 = [[9,9,4],[6,6,8],[2,1,1]]
matrix2 = [[3,4,5],[3,2,6],[2,2,1]]
print(longest_increasing_path(matrix1))
print(longest_increasing_path(matrix2))
print(longest_increasing_path([[1]]))