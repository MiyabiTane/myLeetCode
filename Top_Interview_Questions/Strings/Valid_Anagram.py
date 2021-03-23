class Solution(object):
    def isAnagram(self, s, t):
        def makedic(str_):
            dic = {}
            for s in str_:
                if s in dic:
                    dic[s] += 1
                else:
                    dic[s] = 1
            return dic
        dic1 = makedic(s)
        dic2 = makedic(t)
        return dic1 == dic2

s = "anagram"
t = "nagaram"
sol = Solution()
ans = sol.isAnagram(s,t)
print(ans)
