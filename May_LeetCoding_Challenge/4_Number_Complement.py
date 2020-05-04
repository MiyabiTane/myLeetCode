def findComplement(num: int) -> int:
    ans = 0
    count = 0
    while num > 1:
        ans += abs(num % 2 - 1) * (2 ** count)
        num = num // 2
        count += 1
    return ans

ans = findComplement(1)
print(ans)


