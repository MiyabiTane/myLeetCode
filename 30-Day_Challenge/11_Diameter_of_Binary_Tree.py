# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        def countLen(root, length):
            if (not root.left) and (not root.right):
                return length
            else:
                length += 1
                if root.left and root.right:
                    return max(countLen(root.right,length),countLen(root.left,length))
                elif root.left:
                    return countLen(root.left,length)
                elif root.right:
                    return countLen(root.right,length)
        len = countLen(root, 0)
        return len


            

