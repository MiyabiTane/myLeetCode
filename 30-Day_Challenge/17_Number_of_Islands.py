from collections import deque
#import numpy as np
def numIslands(grid):
    def search(grid, check, i, j):
        qu = deque([(i, j)])
        #BFSで島がつながってるとこを"t"にする。
        while qu:
            i, j = qu.popleft()
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1" and check[i][j] == "f":
                check[i][j] = "t"
                qu.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
                #print(np.array(check))
                #print("")

    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    count = 0
    check = [["f" for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j]=="1" and check[i][j]=="f":
                count+=1 #island１つ発見
                search(grid,check,i,j)
    return count


ans = numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
print(ans)
    

