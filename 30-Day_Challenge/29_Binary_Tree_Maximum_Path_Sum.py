# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        if not root.right and not root.left:
            return root.val
        def countsum(root, sum):
            if not root:
                return sum
            elif not root.right and not root.left:
                return max(sum, root.val, sum+root.val)
            elif not root.right:
                return max(sum, countsum(root.left, sum), countsum(root.left, 0))
            elif not root.left:
                return max(sum, countsum(root.right, sum), countsum(root.right, 0))
            num = root.val
            left = countsum(root.left, 0)
            right = countsum(root.right, 0)
            left_sum = countsum(root.left, sum)
            right_sum = countsum(root.right, sum)
            return max(sum, left_sum, right_sum, num+left+right)

        return countsum(root, root.val)
