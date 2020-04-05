def isHappy(n):
    def Happy(n,rem_sum):
        sum = 0
        while True:
            num = n % 10
            sum += num**2
            if n < 10:
                break
            n = n//10
        if sum in rem_sum:
            return False
        if sum==1:
            return True
        rem_sum.append(sum)
        return Happy(sum,rem_sum)
    return Happy(n,[])
    

ans=isHappy(71)
print(ans)
    

