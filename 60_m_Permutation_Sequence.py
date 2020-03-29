def getPermutation(n, k):
    ans=[]
    #ここからpopすれば数字の重複気にしなくていい
    remain_num=[i+1 for i in range(n)]
    #累乗のリスト
    fact_list = [1]
    for i in range(1, n+1):
        fact_list.append(fact_list[-1]*i)
    #n -> n-len(ans), k -> 残りのk
    def decide_num(n, k):
        fac=fact_list[n]
        count=0
        if k!=fac:
            while k>fac:
                k-=fac
                count+=1
        return count, k
    remain=n-1
    for i in range(n):
        count,k = decide_num(remain, k)
        add_num = remain_num.pop(count)
        ans.append(add_num)
        remain-=1
       
    ans=list(map(str,ans))
    return "".join(ans)

ans=getPermutation(3,3)
print(ans)
