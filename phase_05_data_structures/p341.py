def surronded_regions(board):
    if not board:
        return
    
    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'S'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                dfs(r, c)
        
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'

board = [                                                                                                                             
      ['X','X','X','X'],                                    
      ['X','O','O','X'],
      ['X','X','O','X'],
      ['X','O','X','X']
  ]

surronded_regions(board)
print(board)
    