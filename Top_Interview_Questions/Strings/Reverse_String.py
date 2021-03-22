class Solution(object):
    def reverseString(self, s):
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[-1 * (i+1)]
            s[-1 * (i+1)] = tmp
        return s
