def trailingZeros(n):
    ans=0
    count=1
    while True:
        if n>=5**count:
            ans+=(n//(5**count))
            count+=1
        else:
            break
    return ans
