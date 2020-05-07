# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # keep depth
        keep_x = []
        keep_y = []
        def isCousinsHelper(root, depth):
            flag = 0
            if not root:
                return False
            if root.right:
                if root.right.val == x:
                    flag = 1
                    if depth+1 in keep_y:
                        return True
                    keep_x.append(depth+1)
                if root.right.val == y:
                    flag = 2
                    if depth+1 in keep_x:
                        return True
                    keep_y.append(depth+1)

            if root.left:
                if root.left.val == x:
                    if depth+1 in keep_y:
                        if flag != 2:
                            return True
                    keep_x.append(depth+1)
                if root.left.val == y:
                    if depth+1 in keep_x:
                        if flag != 1:
                            return True
                    keep_y.append(depth+1)
           
            return isCousinsHelper(root.left, depth+1) or isCousinsHelper(root.right, depth+1)

        return isCousinsHelper(root, 0)


