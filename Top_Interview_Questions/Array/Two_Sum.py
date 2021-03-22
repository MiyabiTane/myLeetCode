class Solution(object):
    def twoSum(self, nums, target):
        # make hash table
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        # search
        for i, num in enumerate(nums):
            if target - num in dic:
                ans_ind = dic[target - num]
                if i != ans_ind:  # 自分自身でなければ
                    return [i, ans_ind]
