import numpy as np
def longestCommonSubsequence(text1, text2):
    """
    make the DP matrix row=len(text1),col=len(text2)
    DP(i,j) = DP[i-1][j-1]+1 (text1[i]=text2[j])
              max(DP[i][j-1], DP[i-1][j]) (else)
    """
    m = len(text1); n = len(text2)
    DP = [[0 for _ in range(n)] for _ in range(m)]
    if text1[0] == text2[0]:
        DP[0][0] = 1
    #1行目更新
    for j in range(1,n):
        DP[0][j] = DP[0][j-1]
        if text1[0]== text2[j]:
            DP[0][j] += 1   
    #1列目更新
    for i in range(1,m):
        DP[i][0] = DP[i-1][0]
        if text1[i] == text2[0]:
            DP[i][0] += 1
    #残りの更新
    for i in range(1,m):
        for j in range(1,n):
            if text1[i] == text2[j]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    print(np.array(DP))
    return DP[-1][-1]


ans = longestCommonSubsequence("lcnqdmvsdopkvqvejijcdyxetuzonuhuzkpelmva",
                               "bklgfivmpozinybwlovcnafqfybodkhabyrglsnen")
print(ans)


