def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    m=len(obstacleGrid)
    n=len(obstacleGrid[0])
    obstacleGrid[0][0]=1
    #first row
    for i in range(1,n):
        #論理積　0&1=0, 1&1=1, intつけないとTrue or Falseで返ってくる。
        obstacleGrid[0][i]=int(obstacleGrid[0][i-1]==1 and obstacleGrid[0][i]==0)
    #first col
    for i in range(1,m):
        obstacleGrid[i][0]=int(obstacleGrid[i-1][0]==1 and obstacleGrid[i][0]==0)
    #残りのマス
    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j]==1:
                obstacleGrid[i][j]=0
            else:
                obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
    #print(obstacleGrid)
    return obstacleGrid[m-1][n-1]

ans=uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
print(ans)
