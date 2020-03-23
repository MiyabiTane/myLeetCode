def generateMatrix(n):
        ans=[[0]*n for _ in range(n)]
        seen=[[0]*n for _ in range(n)]
        dr=[0,1,0,-1] #iのまわる方向
        dc=[1,0,-1,0] #jのまわる方向
        r=c=di=0
        for i in range(n*n):
            ans[r][c] = (i+1)
            seen[r][c]=1
            next_r = r+dr[di]
            next_c = c+dc[di]
            if next_r>(n-1) or next_c>(n-1) or seen[next_r][next_c]==1:
                di=(di+1)%4
                next_r = r+dr[di]
                next_c = c+dc[di]
            r = next_r; c = next_c
            #print(r,c)
        return ans
        
ans=generateMatrix(3)
print(ans)