def removeKdigits(num, k):
    num = list(num)
    leng = len(num) - k
    if leng <= 0:
        return "0"
    def Helper(num, leng, ans):
        if leng == 0:
            return ans
        for i in range(0,10):
            if str(i) in num:
                index = num.index(str(i))
                if len(num[index+1:]) >= leng - 1:
                    ans += i * 10**(leng-1)
                    return Helper(num[index+1:], leng - 1, ans)
        
    ans = Helper(num, leng, 0)
    return str(ans)


ans = removeKdigits("1432219", 3)
print(ans)


