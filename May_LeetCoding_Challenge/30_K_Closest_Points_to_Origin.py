def kClosest(points, K):
    max_dist = points[0][0]**2 + points[0][1]**2
    max_pos = points[0]
    ans = [max_pos]
    keep_dist = [max_dist]
    for x, y in points[1:]:
        print(keep_dist)
        dist = x**2 + y**2
        if len(ans) == K:
            if dist < max_dist:
                keep_dist.remove(max_dist)
                ans.remove(max_pos)
                keep_dist.append(dist)
                ans.append([x, y])
        else:
            if dist > max_dist:
                max_dist = dist
                max_pos = [x, y]
            keep_dist.append(dist)
            ans.append([x,y])
                        
    return ans 


ans = kClosest([[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92], [-57, -67]]
               ,5)
print(ans)



