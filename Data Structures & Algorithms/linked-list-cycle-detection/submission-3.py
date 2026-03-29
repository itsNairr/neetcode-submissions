# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = head
        sp = head

        while fp and sp:
            fp = fp.next
            if fp:
                fp = fp.next
            else:
                return False
            sp = sp.next
            if fp is sp:
                return True
        return False