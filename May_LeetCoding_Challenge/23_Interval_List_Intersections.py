def intervalIntersection(A, B):
    leng = max(A[-1][-1], B[-1][-1])
    how_many = [0]*(leng+1)
    ans = []
    for a in A:
        for i in range(a[0], a[1]+1):
            how_many[i] += 1
    for b in B:
        for i in range(b[0], b[1]+1):
            how_many[i] += 1
    print(how_many)
    flag = 0
    for i in range(len(how_many)):
        if how_many[i] == 2 and flag == 0:
            start = i
            flag = 1
        if how_many[i] != 2 and flag == 1:
            end = i-1
            ans.append([start, end]) 
            flag = 0
    return ans


ans = intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [
                           [1, 5], [8, 12], [15, 24], [25, 26]])
print(ans)

