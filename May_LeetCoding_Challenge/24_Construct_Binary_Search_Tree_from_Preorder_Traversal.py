# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        tree = TreeNode(preorder[0])
        stack = [tree]

        for num in preorder[1:]:
            if num < stack[-1].val:
                stack[-1].left = TreeNode(num)
                stack.append(stack[-1].left)
            else:
                while stack and num > stack[-1].val:
                    cur_node = stack.pop()
                cur_node.right = TreeNode(num)
                stack.append(cur_node.right)
        return tree



