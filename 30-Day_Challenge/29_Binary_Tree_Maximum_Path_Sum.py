# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.current_max = float("-inf")

        def maxPathSumHelper(root):
            if not root:
                return 0
            left = maxPathSumHelper(root.left)
            right = maxPathSumHelper(root.right)
            if left <= 0:
                left = 0
            if right <= 0:
                right = 0
            self.current_max = max(left+right+root.val, self.current_max)
            return max(left, right) + root.val

        maxPathSumHelper(root)
        return self.current_max
