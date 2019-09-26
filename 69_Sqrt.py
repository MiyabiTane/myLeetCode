def mySqrt(x):
    ans=0
    while True:
        ans+=1
        if ans*ans>x:
            break
    return ans-1
