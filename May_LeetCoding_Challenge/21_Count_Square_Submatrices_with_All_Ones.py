def countSquares(matrix) -> int:
    n = len(matrix)
    m = len(matrix[0])
    for r in range(1,n):
        for c in range(1,m):
            if matrix[r][c] == 1:
                num = min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1])
                matrix[r][c] = num + 1
    print(matrix)
    one_dim_list = sum(matrix, [])
    return sum(one_dim_list)


ans = countSquares([
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
])
print(ans)
