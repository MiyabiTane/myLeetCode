class Solution(object):
    def twoSum(self, nums, target):
        rtype=[]
        self.nums=nums
        self.target=target
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                #print("n[i]: %d  n[j]: %d"%(self.nums[i],self.nums[j]))
                if self.nums[i]+self.nums[j]==self.target:
                    #print("find pair")
                    rtype.append(i)
                    rtype.append(j)
        return rtype


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
