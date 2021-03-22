# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            jud = isBadVersion(mid)
            if jud:
                start = mid + 1
            else:
                end = mid
        return start
