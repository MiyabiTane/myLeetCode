def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True
    cand = num // 2
    for i in range(cand, 0, -1):
        if num % cand == 0:
            if num / cand == cand:
                return True
        cand -= 1
    return False

ans = isPerfectSquare(14)
print(ans)