class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def isSymmetric(self,root):
        return self.check(root,root)

    #check wether t2 is mirror of t1
    def check(self,t1,t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        elif t1.val==t2.val:
            if self.check(t1.left,t2.right) and self.check(t1.right,t2.left):
                return True
        return False
