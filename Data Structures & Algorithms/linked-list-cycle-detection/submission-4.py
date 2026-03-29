# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fp = head
        sp = head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            if fp is sp:
                return True
        return False