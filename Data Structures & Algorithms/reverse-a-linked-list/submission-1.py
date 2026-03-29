# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev):
            if node is None:
                return prev
            temp = node.next
            node.next = prev
            prev = node
            return reverse(temp, prev) 
        return reverse(head, None)