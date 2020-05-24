class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            if p.val==q.val:
                if self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left):
                    return True
            else:
                return False
