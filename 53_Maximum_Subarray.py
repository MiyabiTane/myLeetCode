#dynamic Solution
#max(now_position,sum_before+now_position)
def maxSubArray(nums):
    max_sum=[]
    sum_before=-float('inf')
    for num in nums:
        max_sum.append(max(num,sum_before+num))
        sum_before=max_sum[-1]
    return max(max_sum)
