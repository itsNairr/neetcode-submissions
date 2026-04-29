# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global summ
        summ = 0
        def backtrack(node):
            global summ
            if not node:
                return False
            if not node.left and not node.right:
                return summ + node.val == targetSum
            
            summ += node.val
            if backtrack(node.left):
                return True
            if backtrack(node.right):
                return True
            summ -= node.val
            return False

        return backtrack(root)