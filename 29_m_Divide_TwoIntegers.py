def divide(dividend,divisor):
    sig=1
    if dividend<0:
        dividend*=(-1)
        sig*=(-1)
    if divisor<0:
        divisor*=(-1)
        sig*=(-1)
    count=0
    while dividend>=divisor:
        dividend-=divisor
        count+=1
    if sig==(-1):
        count*=(-1)
    return count

ans=divide(7,-3)
print(ans)
