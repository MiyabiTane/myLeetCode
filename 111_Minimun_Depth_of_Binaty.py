class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution(object):
    def minDepth(self,root):
        if root==None:
            return 0
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
