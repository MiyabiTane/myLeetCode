class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def isBalanced(self,root):
        if not root:
            return True
        elif abs(self.maxcount(root.left)-self.maxcount(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        """
        #[1,2,2,3,null,null,3,4,null,null,4]->True but actually the answer is False
        elif abs(self.maxcount(root.left)-self.maxcount(root.right))<=1:
            return True
        else:
            return False"""

    def maxcount(self,root):
        if not root:
            return 0
        else:
            return max(self.maxcount(root.left),self.maxcount(root.right))+1
