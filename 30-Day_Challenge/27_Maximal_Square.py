import numpy as np
def maximalSquare(matrix):
    max_len = 0
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    DP = [[0 for _ in range(n)] for _ in range(m)]
    #1行目更新
    for i in range(n):
        if matrix[0][i] == '1':
            DP[0][i] = 1
            if max_len < DP[0][i]:
                max_len = DP[0][i]
    #1列目更新
    for i in range(1, m):
        if matrix[i][0] == '1':
            DP[i][0] = 1
            if max_len < DP[i][0]:
                max_len = DP[i][0]
    #残り更新
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1
                if max_len < DP[i][j]:
                    max_len = DP[i][j]
    #print(np.array(matrix))
    #print(np.array(DP))
    return max_len**2


ans = maximalSquare([["0", "0", "0", "1"], ["1", "1", "0", "1"], [
                    "1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]])
print(ans)
