def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_dict = {}
    for s in magazine:
        if s in mag_dict:
            mag_dict[s] += 1
        else:
            mag_dict[s] = 1
    for st in ransomNote:
        if st in mag_dict:
            if mag_dict[st] > 0:
                mag_dict[st] -= 1
            else:
                return False
        else:
            return False
    return True

ans = canConstruct("aa", "ab")
print(ans)


