def singleNonDuplicate(nums):
    candidate = nums[-1]
    for i, num in enumerate(nums):
        if not num == candidate:
            if i % 2 == 1:
                return candidate
            candidate = num

    return candidate


ans = singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
print(ans)




