# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        fut = None
        temp = head
        while temp is not None:
            fut = temp.next
            temp.next = prev
            prev = temp
            if fut is None:
                head = temp
            temp = fut
        return head