# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root, arr):
        memo = {}
        n = len(arr)
        def DFS(cur_node, cur_arr, arr):
            if cur_arr == n-1:
                if cur_node.val == arr[cur_arr]:
                    if not cur_node.left or not cur_node.right:
                        memo[(cur_node, cur_arr)] = 1 #True
                    else:
                        memo[(cur_node, cur_arr)] = 0 #False
            elif not cur_node.left and not cur_node.right:
                memo[(cur_node, cur_arr)] = 0
            elif not (cur_node, cur_arr) in memo:
                if cur_node.val == arr[cur_arr] and DFS(cur_node.left):
                    memo[(cur_node, cur_arr)] = 1
                else:
                    memo[cur_node, cur_arr]
                



            if cur_arr = len(arr) - 1:
                if cur_arr.left == arr[-1] or cur_arr.right == arr[-1]:
                    return True
            





