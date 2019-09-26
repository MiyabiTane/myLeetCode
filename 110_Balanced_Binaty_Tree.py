class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def isBalanced(self,root):
        count=0
        if not root:
            return True

        self.iscount(root.left,count,1)
        self.iscount(root.right,count,-1)

        if -1<=count<=1:
            return True
        elif count<-1 or 1<count:
            return False

    def iscount(self,root,count,num):
        if root:
            count+=num
            return count

"""
mugen roop
class Solution(object):
    def isBalanced(self,root):
        count=0
        if not root:
            return True
        while root:
            if root.left:
                count+=1
            elif root.right:
                count-=1
        if -1<=count<=1:
            return True
        else:
            return False"""
