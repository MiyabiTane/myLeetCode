def kClosest(points, K):

    def partition(points, l, r):
        #一番右側の数字で分ける（左：小さい、右：大きい）時にその数字がどこにくるか
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]
        return a


    def QuickSort(points, l, r, K):
        if l < r:
            p = partition(points, l, r)
            if p == K:
                return
            elif p < K:
                QuickSort(points, p+1, r, K)
            else:
                QuickSort(points, l, p-1, K)

    QuickSort(points, 0, len(points) - 1, K)
    return points[:K]


ans = kClosest([[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38],
                [-73, -74], [-55, -39], [62, 91], [62, 92], [-57, -67]], 5)
print(ans)

#参考動画：https: // www.youtube.com/watch?v = ywWBy6J5gz8

