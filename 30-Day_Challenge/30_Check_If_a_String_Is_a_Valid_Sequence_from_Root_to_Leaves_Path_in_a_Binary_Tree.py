# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root, arr):
        def Helper(cur_node, cur_index, arr):
            if not cur_node:
                if len(arr) != 0:
                    return False
            if cur_index == len(arr) - 1:
                if cur_node.val == arr[cur_index] and not cur_node.left and not cur_node.right:
                    return True
            elif cur_index < len(arr) - 1 and cur_node.val == arr[cur_index]:
                return Helper(cur_node.left, cur_index+1, arr) or Helper(cur_node.right, cur_index+1, arr)
        return Helper(root, 0, arr)



            




