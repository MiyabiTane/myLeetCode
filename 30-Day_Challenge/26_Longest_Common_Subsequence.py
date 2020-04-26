import numpy as np
def longestCommonSubsequence(text1, text2):
    """
    make the DP matrix row=len(text1),col=len(text2)
    DP(i,j) = DP[i-1][j-1]+1 (text1[i]=text2[j])
              max(DP[i][j-1], DP[i-1][j]) (else)
    """
    m = len(text1); n = len(text2)
    DP = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    print(np.array(DP))
    return DP[-1][-1]


ans = longestCommonSubsequence("lcnqdmvsdopkvqvejijcdyxetuzonuhuzkpelmva",
                               "bklgfivmpozinybwlovcnafqfybodkhabyrglsnen")
print(ans)


