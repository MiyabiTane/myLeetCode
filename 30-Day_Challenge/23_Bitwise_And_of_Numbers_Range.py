import math
def rangeBitwiseAnd(m, n):
    k = 0
    #数字が連続していることに注目する
    while n != m:
        n //= 2
        m //= 2
        k += 1
    return n * (2**k)

ans = rangeBitwiseAnd(5,7)
print(ans) 