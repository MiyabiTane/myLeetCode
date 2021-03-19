# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        def levelOrder_(root, count, lst):
            if not root:
                return lst
            if len(lst) - 1 > count:
                lst.append([])
            lst[count].append(root.val)
            lst = levelOrder_(root.left, count + 1, lst)
            lst = levelOrder_(root.right, count + 1, lst)
            return lst
        levelOrder_(root, 0, [])