# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
                slow = slow.next

        fast = slow.next
        slow.next = None
        pre = None
        after = fast.next

        while fast:
            fast.next = pre
            pre = fast
            if after:
                fast = after
                after = after.next
            else:
                break

        slow = head
        afters = slow.next
        afterf = fast.next

        while slow:
            slow.next = fast
            if fast:
                fast.next = afters
            slow = afters
            fast = afterf
            if afters:
                afters = afters.next
            if afterf:
                afterf = afterf.next
        

        