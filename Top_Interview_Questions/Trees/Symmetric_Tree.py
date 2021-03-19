# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def isSame(root1, root2):
            if (not root1) and (not root2):
                return True
            elif (not root1) or (not root2):
                return False
            else:
                if root1.val == root2.val and isSame(root1.left, root2.right) and isSame(root1.right, root2.left):
                    return True
                else:
                    return False

        return isSame(root, root)
