def word_search(board, word):
    rows, cols = len(board), len(board[0])
    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (backtrack(r+1,c,idx+1) or backtrack(r-1,c,idx+1) or
                 backtrack(r,c+1,idx+1) or backtrack(r,c-1,idx+1))
        board[r][c] = temp
        return found
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(word_search(board, "ABCCED"))
print(word_search(board, "SEE"))
print(word_search(board, "ABCB"))