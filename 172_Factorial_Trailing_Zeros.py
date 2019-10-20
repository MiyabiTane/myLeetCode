import math

def trailingZeros(n):
    n_fac=math.factorial(n)
    ans=0
    amari=n_fac%10
    while amari==0:
        ans+=1
        n_fac/=10
        amari=n_fac%10
    return ans
