# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenn = 1
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next
            if (lenn >= n):
                prev = slow
                slow = slow.next
            lenn+= 1
        if (lenn >= n):
            if prev:
                prev.next = slow.next
            if slow is head:
                head = slow.next
            slow.next = None
            return head
        return None