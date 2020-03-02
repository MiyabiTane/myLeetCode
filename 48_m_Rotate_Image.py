def rotate(matrix):
    #iとjを入れ替え
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[0])):
            tmp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=tmp
    #print(matrix)
    #各行の左右を入れ替え
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix

ans=rotate([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(ans)
