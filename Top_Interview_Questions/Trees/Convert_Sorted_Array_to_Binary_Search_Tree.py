# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def makeBST(root, nums):
            if not nums:
                return root
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            print(root.val, root.left, root.right)
            makeBST(root.left, nums[:mid])
            makeBST(root.right, nums[mid+1:])
        if not nums:
            return None
        root = TreeNode()
        root = makeBST(root, nums)
        return root
