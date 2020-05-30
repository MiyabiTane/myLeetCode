def maxUncrossedLines(A, B):
    #dummyを頭につける。数字はなんでも良い。
    A = [0] + A; B = [0] + B
    dp_table = {}

    def recursion(idx_a, idx_b):

        if (idx_a, idx_b) in dp_table:
            return dp_table[(idx_a, idx_b)]

        #dummy部分はline0個
        if idx_a == 0 or idx_b == 0:
            return 0
        
        elif A[idx_a] == B[idx_b]:
            dp_table[(idx_a, idx_b)] = recursion(idx_a-1, idx_b-1) + 1
            return dp_table[(idx_a, idx_b)]
        
        else:
            dp_table[(idx_a, idx_b)] = max(recursion(idx_a, idx_b-1), recursion(idx_a-1, idx_b))
            return dp_table[(idx_a, idx_b)]
    
    return recursion(len(A)-1, len(B)-1)
              

ans = maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])
print(ans)

