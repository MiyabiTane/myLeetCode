def getRow(rowIndex):
    #init
    ans=[1 for j in range(rowIndex+1)]
    #c(i,j)=i!/(j!*(n-j)!)
    #c(i-1,j)=c(i,j)*(i-j)/i
    if rowIndex>1:
        for i in range(1,rowIndex//2+1):
            ans[i]=ans[rowIndex-i]=ans[i-1]*(rowIndex-i+1)/i
    return ans


    """rowIndex+=1
    if rowIndex==0:
        return []
    #init
    ans=[[1 for i in range(1,j+2)] for j in range(rowIndex)]
    for i in range(rowIndex):
        if i>1:
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
    return ans[-1]"""
