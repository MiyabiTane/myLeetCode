def maxUncrossedLines(A, B):
    n = len(A)
    m = len(B)
    #１行１列０パディング
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if A[i] == B[j]: 
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]


ans = maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])
print(ans)
