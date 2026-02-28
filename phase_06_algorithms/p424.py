def set_zeroes(matrix):
    zero_rows = set()
    zero_cols = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0


m1 = [[1,1,1],[1,0,1],[1,1,1]]
m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

set_zeroes(m1)
print(m1)

set_zeroes(m2)
print(m2)