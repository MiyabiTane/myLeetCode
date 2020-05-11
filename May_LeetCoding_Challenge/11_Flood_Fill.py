def floodFill(image, sr, sc, newColor):
    n = len(image)
    m = len(image[0])
    originalColor = image[sr][sc]
    #この時、出発点との間を永遠にループしてしまう
    if originalColor == newColor:
        return image
    def floodFillHelper(x, y):
        if image[x][y] == originalColor:
            image[x][y] = newColor
            if x > 0:
                floodFillHelper(x-1, y)
            if y > 0:
                floodFillHelper(x, y-1)
            if x < n-1:
                floodFillHelper(x+1, y)
            if y < m-1:
                floodFillHelper(x, y+1)

    floodFillHelper(sr, sc) 
    return image


ans = floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
print(ans)
