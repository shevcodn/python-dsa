def solve_n_queens(n):
    result = []
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row, board):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = 'Q'
            backtrack(row + 1, board)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    board = [['.'] * n for _ in range(n)]
    backtrack(0, board)
    return result

solutions = solve_n_queens(4)
print(len(solutions))
for s in solutions:
    print(s)



    
