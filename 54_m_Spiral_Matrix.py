def spiralOrder(matrix):
    if matrix==[]:
        return []
    #どこをすでに通ったかの記録
    R,C=len(matrix),len(matrix[0])
    seen=[[0]*C for _ in matrix]
    dr=[0,1,0,-1] #iの回る方向
    dc=[1,0,-1,0] #jの回る方向

    ans=[]
    r=c=di=0
    for i in range(R*C):
        ans.append(matrix[r][c])
        seen[r][c]=1
        next_r=r+dr[di]
        next_c=c+dc[di]
        if 0<=next_r<R and 0<=next_c<C and seen[next_r][next_c]==0:
            r=next_r; c=next_c
        else:
            di=(di+1)%4
            r=r+dr[di]
            c=c+dc[di]
    return ans
    

ans=spiralOrder([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(ans)