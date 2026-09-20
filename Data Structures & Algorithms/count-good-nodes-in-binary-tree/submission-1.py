# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        mono = []

        def dfs(node):
            nonlocal count, mono

            if not node:
                return
            if not mono or node.val >= mono[-1]:
                count += 1
                mono.append(node.val)
            dfs(node.left)
            dfs(node.right)
            if node.val == mono[-1]:
                mono.pop()
        dfs(root)
        return count
            