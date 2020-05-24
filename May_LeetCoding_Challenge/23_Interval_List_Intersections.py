def intervalIntersection(A, B):
    p_a = 0; p_b = 0
    ans = []
    while p_a < len(A) and p_b < len(B):
        start = max(A[p_a][0], B[p_b][0])
        end = min(A[p_a][1], B[p_b][1])

        if start <= end:
            ans.append([start, end])
        
        if A[p_a][1] <= B[p_b][1]:
            p_a += 1
        else:
            p_b += 1
    return ans


ans = intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [
                           [1, 5], [8, 12], [15, 24], [25, 26]])
print(ans)

