# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0

        def countLen(root):
            if not root:
                return 0
            left = countLen(root.left)
            right = countLen(root.right)
            self.length = max(self.length, left+right)
            return max(left,right)+1
        
        countLen(root)
        return self.length
