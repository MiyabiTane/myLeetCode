def minDistance(word1, word2):
    n = len(word1) + 1
    m = len(word2) + 1
    dp = [[0 for _ in range(m)] for _ in range(n)]

    #１行目更新
    for i in range(m):
        dp[0][i] = i
    #１列目更新
    for j in range(1, n):
        dp[j][0] = j
        
    for i in range(1, n):
        for j in range(1, m):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    #print(dp)
    return dp[-1][-1]


ans = minDistance("intention", "execution")
print(ans)


#解説動画：https://www.youtube.com/watch?v=OCsF6u-bLBc
