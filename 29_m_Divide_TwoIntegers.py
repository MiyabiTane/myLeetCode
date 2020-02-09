def divide(dividend,divisor):
    sig=1
    if dividend<0:
        dividend*=(-1)
        sig*=(-1)
    if divisor<0:
        divisor*=(-1)
        sig*=(-1)

    if dividend<divisor:
        return 0

    count=0
    multipular=1
    #dividendをdivrで割れる最大の回数(偶数回)
    while dividend>=(divisor<<1):
        #つまり*2
        divisor=divisor<<1
        multipular*=2
    #答え
    while multipular>=1 and dividend>0:
        if dividend-divisor>=0:
            dividend-=divisor
            count+=multipular
        #つまり//2
        divisor=divisor>>1
        multipular=multipular>>1

    if sig==(-1):
        count*=(-1)
    if count<(-2)**31:
        return (-2)**31
    elif count>2**31-1:
        return 2**31-1
    return count

#ビット　参考:https://www.javadrive.jp/python/num/index4.html#section1-5

ans=divide(7,-3)
print(ans)
