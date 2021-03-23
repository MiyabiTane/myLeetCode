class Solution(object):
    def reverse(self, x):
        neg_flag = False
        if x < 0:
            neg_flag = True
            x *= -1
        ans = ""
        while x > 0:
            ans += str(x % 10)
            x = x // 10
        ans = int(ans)
        if neg_flag:
            return -1*ans
        return ans