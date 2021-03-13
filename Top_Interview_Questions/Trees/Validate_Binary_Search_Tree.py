import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        def isValid(root, low, high):
            if not root:
                return True
            elif root.val <= low or root.val >= high:
                return False
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, high)
        return isValid(root, -2**31-1, 2**31)
