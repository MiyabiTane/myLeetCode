class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def isSymmetric(self,root):
        q=[]
        q.append(self.left.val)
        if self.right.val==q[-1]:
