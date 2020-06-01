def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    if n == 0:
        return m
    if m == 0:
        return n
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 0 if word1[0] == word2[0] else 1

    #１行目更新
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] if word2[i] == word1[0] else dp[0][i-1] + 1
    #１列目更新
    for j in range(1, n):
        dp[j][0] = dp[j-1][0] if word2[0] == word1[j] else dp[j-1][0] + 1
        
    for i in range(1, n):
        for j in range(1, m):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    #print(dp)
    return dp[-1][-1]


ans = minDistance("intention", "execution")
print(ans)


#解説動画：https://www.youtube.com/watch?v=OCsF6u-bLBc
