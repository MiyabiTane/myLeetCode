def minPathSum(grid):
    m = len(grid); n = len(grid[0])
    #1列目更新
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    #1行目更新
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    #残りの更新
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    print(grid)
    return grid[-1][-1]


ans = minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
])
print(ans)


