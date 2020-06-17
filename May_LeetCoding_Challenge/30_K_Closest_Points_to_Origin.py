def kClosest(points, K):
    points.sort(key = lambda P:P[0]**2 + P[1]**2)
    return points[:K]

ans = kClosest([[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92], [-57, -67]]
               ,5)
print(ans)



