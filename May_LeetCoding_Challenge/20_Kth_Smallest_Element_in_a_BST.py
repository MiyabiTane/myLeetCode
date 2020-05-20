# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def Helper(root):
            if not root:
                return []
            return Helper(root.left) + [root.val] + Helper(root.right) 
        num_list = Helper(root)
        num_list = sorted(num_list)
        return num_list[k-1]