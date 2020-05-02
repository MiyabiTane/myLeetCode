def numJewelsInStones(J: str, S: str) -> int:
    jewel = 0
    for s in S:
        if s in J:
            jewel += 1
    return jewel


ans = numJewelsInStones("zz","ZZZ")
print(ans)


