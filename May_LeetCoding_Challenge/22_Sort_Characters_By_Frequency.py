from collections import Counter 
def frequencySort(s: str) -> str:
    ans_str = ''
    num_frequency = Counter(s)
    num_frequency = sorted(num_frequency.items(), key=lambda x: x[1], reverse=True)
    #print(num_frequency)
    for items in num_frequency:
        count = items[1]
        while count > 0:
            ans_str += items[0]
            count -= 1
    return ans_str


ans = frequencySort("Aabb")
print(ans)


