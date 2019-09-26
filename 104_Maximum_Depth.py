class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


"""class Solution(object):
    def maxDepth(self,root):
        dep=0
        if root.val:
            dep+=1
            return max((self.maxDepth(root.left)),(root.maxDepth(self.right)))
        else:
            return dep"""

class Solution(object):
    def maxDepth(self,root):
        if root==None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
