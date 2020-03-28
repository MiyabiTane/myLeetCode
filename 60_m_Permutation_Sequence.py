def getPermutation(n, k):
    def factoral(num):
        if num==0 or num==1:
            return 1
        ans = 1
        while True:
            ans *= num
            num -= 1
            if num == 1:
                return ans
    def getPermutation_sub(lst, n, k, p):
        if p==n-1:
            while lst[p] in lst[:p]:
                lst[p] += 1
            return lst
        num=factoral(n-1-p)
        if num>=k:
            while lst[p] in lst[:p]:
                lst[p]+=1
            return getPermutation_sub(lst, n, k, p+1)
        else:
            lst[p]+=1
            while lst[p] in lst[:p]:
                lst[p]+=1
            k-=num
            if k==0:
                return lst
            return getPermutation_sub(lst, n, k, p)
    init_lst=[1]*n
    ans=getPermutation_sub(init_lst, n, k ,0)
    ans=list(map(str,ans))
    return "".join(ans)

ans=getPermutation(3,2)
print(ans)
