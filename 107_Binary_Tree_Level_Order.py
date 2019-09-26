class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def levelOrderBottom(self,root):
        ans=[]
        self.levelOrder(root,ans,0)
        ans.reverse()
        return ans

    def levelOrder(self,root,ans,level):
        if root:
            if level>=len(ans):
                ans.append([])
            ans[level].append(root.val)
            self.levelOrder(root.left,ans,level+1)
            self.levelOrder(root.right,ans,level+1)


""">>> a=[[1,2],[3,4],[]]
>>> a[2].append(5)
>>> a[2].append(6)
>>> a
[[1, 2], [3, 4], [5, 6]]"""
