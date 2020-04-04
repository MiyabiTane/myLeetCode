import math
def uniquePathsWithObstacles(obstacleGrid):
    m=len(obstacleGrid)
    n=len(obstacleGrid[0])
    def findObstacle(obstacleGrid):
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    return i+1,j+1
        return False

    def uniquePaths(m,n):
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))

    answer = uniquePaths(m, n)
    if findObstacle(obstacleGrid):
        ob_m, ob_n = findObstacle(obstacleGrid)
        start_to_ob = uniquePaths(ob_m, ob_n)
        ob_to_fin = uniquePaths(m-ob_m+1, n-ob_n+1)
        answer -= (start_to_ob+ob_to_fin)
    return answer

init_list=[[0,0,0],[0,1,0],[0,0,0]]
ans=uniquePathsWithObstacles(init_list)
print(ans)

