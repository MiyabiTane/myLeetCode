def climbStairs(n):
    ans=[0]*(n+1)
    for i in range(1,n+1):
        if i==1 or i==2:
            ans[i]=i
        else:
            ans[i]=ans[i-1]+ans[i-2]
        #print(ans)
    return ans[-1]
