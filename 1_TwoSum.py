class Solution(object):
    def twoSum(self, nums, target):
        rtype=[]
        dict={}
        self.nums=nums
        self.target=target

        #get dictionary
        for i in range(len(self.nums)):
            dict[self.nums[i]]=i

        #search
        for i in range(len(self.nums)):
            comp=self.target-nums[i]
            if (comp in dict) and (dict.get(comp)!=i):
                rtype=[i,dict.get(comp)]
                return rtype

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
