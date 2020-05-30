def countBits(num):
    #divide num in groups 1:[0,1], 2:[2-4], 4:[5-8], 8:[9-15] ...
    group = 1
    ans = [0]
    for i in range(1, num+1):
        if i == group * 2:
            group *= 2
        ans.append(ans[i-group] + 1)
    return ans

ans = countBits(5)
print(ans)

