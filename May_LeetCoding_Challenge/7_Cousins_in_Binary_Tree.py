# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Each node has a unique integer value from 1 to 100.
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def DFS(node, parent, depth, mod):
            if node:
                if node.val == mod:
                    return depth, parent
                return DFS(node.left, node, depth+1, mod) or DFS(node.right, node, depth+1, mod)
        #右辺はtuple型で(depth, parent, depth, parent)
        dx, px, dy, py = DFS(root, None, 0, x) + DFS(root, None, 0, y)
        return dx == dy and px != py
            
