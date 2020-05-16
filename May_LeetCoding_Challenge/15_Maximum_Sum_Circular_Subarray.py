from collections import deque
def maxSubarraySumCircular(A):
    n = len(A)
    B = A+A
    P = [0]
    #P[j] = sum B[:j]
    for num in B:
        P.append(P[-1] + num)
    #1 <= j-i <= N を満たす最大のP[j]-P[i]を求める
    # -> P[j]に対して j-N <= i を満たす最小のP[i]を求める
    ans = A[0]
    qu = deque([0]) #iの現在値
    for j in range(1, len(P)):
        # j-N <= i を満たさないiは調べない
        if qu[0] < j-n:
            qu.popleft()
        
        ans = max(ans, P[j]-P[qu[0]])
        
        # P[i2] <= P[i1]となるようなi1は取り除く
        while qu and P[j] <= P[qu[-1]]:
            qu.pop()
        qu.append(j)
    return ans


ans = maxSubarraySumCircular([5, -3, 4])
print(ans)

