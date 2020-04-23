import math
def rangeBitwiseAnd(m, n):
    if m == 0:
        return 0
    if n == 1 and m == 1:
        return 1
    min = int(math.log2(m)) #一番小さい数の桁数-1
    ans = 0
    for i in range(min): #一桁ずつ見る
        print("")
        print(i)
        flag = 0
        for j in range(m, n+1):
            print("j is ",j)
            print("bit is",j%(2**(i+1)))
            if (j%(2**(i+1)))%2 == 0:
                flag = 1
                break
        if flag == 0:
            ans += 2**i
        print("ans = ",ans)
    flag = 0
    for j in range(m, n+1): #最上桁
        print(j)
        print(min)
        if j//(2**min) == 0 or j <= (2**min):
            flag = 1
            break
    if flag == 0:
        ans += 2**min

    return ans        

ans = rangeBitwiseAnd(1,2)
print(ans)