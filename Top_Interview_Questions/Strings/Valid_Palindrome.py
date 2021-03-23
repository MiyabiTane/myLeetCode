class Solution(object):
    def isPalindrome(self, s):
        s = s.replace(' ', '')
        s = s.lower()
        # print(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # print(s[left], s[right])
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


s = "A man, a plan, a canal: Panama"
sol = Solution()
ans = sol.isPalindrome(s)
print(ans)
