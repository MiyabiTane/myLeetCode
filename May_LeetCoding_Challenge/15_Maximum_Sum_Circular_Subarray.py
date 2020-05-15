def maxSubarraySumCircular(A):
    leng = len(A)
    A += A[:-1]
    start = 0; end = 0
    max_list = [A[0]]
    for i in range(1, len(A)):
        end = i
        if A[i] > max_list[-1]+A[i]:
            start = i
            max_list.append(A[i])
        else:
            max_list.append(max_list[-1]+A[i])
        if end - start == leng-1:
            max_list.append(A[i])
            start = i
    return max(max_list)


ans = maxSubarraySumCircular([-2, -3, -1])
print(ans)

