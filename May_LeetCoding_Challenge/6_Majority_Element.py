import collections
def majorityElement(nums):
    dict = collections.Counter(nums)
    ans = [k for k, v in dict.items() if v > len(nums)//2][0]
    return ans


ans = majorityElement([3,2,3])
print(ans)
