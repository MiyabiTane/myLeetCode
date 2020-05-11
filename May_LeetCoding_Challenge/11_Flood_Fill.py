def floodFill(image, sr, sc, newColor):
    n = len(image)
    m = len(image[0])
    originalColor = image[sr][sc]
    seen = [0] * (n*m)
    def floodFillHelper(x, y):
        seen[x + 3*y] = 1
        if image[x][y] == originalColor:
            image[x][y] = newColor
        print(seen)
        if not 0 in seen:
            return image
        else:
            return floodFillHelper(max(x-1, 0), y), floodFillHelper(min(x+1, n-1), y), floodFillHelper(x, max(y-1, 0)), floodFillHelper(x, min(y+1, m-1))
    floodFillHelper(sr, sc) 
    return image


ans = floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
print(ans)
