class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[m:] + nums1[:m]
        cur_ind = 0
        keep_i = -1
        for i, num in enumerate(nums2):
            while nums1[cur_ind] <= num:
                if cur_ind == m + n - 1:
                    keep_i = i
                    break
                cur_ind += 1
            if keep_i != -1:
                # print(keep_i)
                nums1 = nums1[keep_i + 1:] + nums2[keep_i:]
                # print(nums1, cur_ind)
                break
            nums1 = nums1[1: cur_ind] + [num] + nums1[cur_ind:]
            cur_ind -= 1
           #  print(nums1, cur_ind)


sol = Solution()
sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
