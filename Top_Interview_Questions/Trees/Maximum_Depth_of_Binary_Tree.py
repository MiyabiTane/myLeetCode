class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def CountDepth(self, root, count):
        if root.left and root.right:
            return max(self.CountDepth(root.left, count+1), self.CountDepth(root.right, count+1))
        elif root.left:
            return self.CountDepth(root.left, count+1)
        elif root.right:
            return self.CountDepth(root.right, count+1)
        else:
            return count

    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return self.CountDepth(root, 1)
