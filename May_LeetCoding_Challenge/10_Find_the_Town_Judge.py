import numpy as np
def findJudge(N, trust):
    if not trust:
        if N == 1:
            return 1
        return -1
    trust = np.array(trust)
    follower = trust[:, 0]
    obeyed = (trust[:, 1]).tolist()
    candidate = []
    for i in range(N):
        if not i+1 in follower:
            candidate.append(i+1)
    #print(candidate)
    if not candidate:
        return -1
    for c in candidate:
        if obeyed.count(c) == N-1:
            return c
    return -1


ans = findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
print(ans)

