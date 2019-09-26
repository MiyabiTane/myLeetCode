class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.ledt=None
        self.right=None

class Solution(object):
    def hasPathSum(self,root,sum):
        if not root:
            return False
        elif
        else:
            if root.val==sum and ((not root.left) and (not root.right)):
                return True
            else:
                return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
