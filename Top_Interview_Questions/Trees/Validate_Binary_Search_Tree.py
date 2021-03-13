# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        else:
            if root.left:
                if root.val <= root.left.val:
                    return False
            if root.right:
                if root.val >= root.right.val:
                    return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

        
