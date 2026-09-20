# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        self.arr = []
        self.i = 0
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.arr.append(curr.val)
                curr = curr.right

    def next(self) -> int:
        val = self.arr[self.i]
        self.i += 1
        return val

    def hasNext(self) -> bool:
        return True if self.i < len(self.arr) else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()