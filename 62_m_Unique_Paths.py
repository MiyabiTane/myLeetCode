import math
def uniquePaths(m, n):
    ans=math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))
    return int(ans)
    
ans=uniquePaths(3,2)
print(ans)