def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    #1行目更新
    for i in range(1,n):
        grid[0][i] += grid[0][i-1]
    #1列目更新
    for i in range(1,m):
        grid[i][0] += grid[i-1][0]
    #残りのマスの更新
    for i in range(1,m):
        for j in range(1,n):
            new_n1 = grid[i][j] + grid[i-1][j]
            new_n2 = grid[i][j] + grid[i][j-1]
            grid[i][j] = min(new_n1, new_n2)
    return grid[m-1][n-1]


ans = minPathSum([[1, 3, 1, 1],
                 [1, 5, 1, 1],
                 [4, 2, 1, 1]])
print(ans)

